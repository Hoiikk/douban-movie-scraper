import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import re

class DoubanDetailedScraper:
    def __init__(self):
        self.base_url = "https://movie.douban.com/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://movie.douban.com/',
        }
    
    def get_weekly_ranking(self):
        """获取一周口碑榜前10名电影的基本信息"""
        try:
            print("正在获取一周口碑榜...")
            response = requests.get(self.base_url, headers=self.headers, timeout=15)
            response.raise_for_status()
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.text, 'html.parser')
            movies = []
            
            # 查找一周口碑榜的表格
            ranking_tables = soup.find_all('table')
            for table in ranking_tables:
                rows = table.find_all('tr')
                if len(rows) >= 5:
                    table_movies = []
                    for row in rows:
                        cells = row.find_all('td')
                        if len(cells) >= 2:
                            rank = cells[0].get_text(strip=True)
                            movie_link = cells[1].find('a')
                            if movie_link and rank.isdigit():
                                movie_name = movie_link.get_text(strip=True)
                                movie_url = movie_link.get('href', '')
                                if movie_name and movie_url:
                                    # 提取电影ID
                                    movie_id = ''
                                    if movie_url:
                                        id_match = re.search(r'/subject/(\d+)/', movie_url)
                                        if id_match:
                                            movie_id = id_match.group(1)
                                    
                                    table_movies.append({
                                        'rank': rank,
                                        'movie_name': movie_name,
                                        'movie_id': movie_id,
                                        'movie_url': movie_url
                                    })
                    
                    if len(table_movies) >= 5:
                        movies = table_movies
                        break
            
            return movies
            
        except Exception as e:
            print(f"获取榜单时出错: {e}")
            return []
    
    def get_movie_details(self, movie_id, movie_name):
        """获取电影详细信息"""
        if not movie_id:
            return {}
        
        try:
            movie_url = f"https://movie.douban.com/subject/{movie_id}/"
            print(f"正在获取《{movie_name}》的详细信息...")
            
            response = requests.get(movie_url, headers=self.headers, timeout=15)
            response.raise_for_status()
            response.encoding = 'utf-8'
            
            soup = BeautifulSoup(response.text, 'html.parser')
            details = {}
            
            # 获取豆瓣评分
            rating_element = soup.find('strong', class_='ll rating_num')
            if rating_element:
                details['rating'] = rating_element.get_text(strip=True)
            else:
                # 尝试其他评分元素
                rating_element = soup.find('span', class_='rating_num')
                if rating_element:
                    details['rating'] = rating_element.get_text(strip=True)
                else:
                    details['rating'] = '暂无评分'
            
            # 获取导演
            director_element = soup.find('a', rel='v:directedBy')
            if director_element:
                details['director'] = director_element.get_text(strip=True)
            else:
                details['director'] = '未知'
            
            # 获取主演（前3个）
            actors = []
            actor_elements = soup.find_all('a', rel='v:starring')
            for actor in actor_elements[:3]:
                actors.append(actor.get_text(strip=True))
            if actors:
                details['actors'] = ', '.join(actors)
            else:
                details['actors'] = '未知'
            
            # 获取年份
            year_element = soup.find('span', class_='year')
            if year_element:
                details['year'] = year_element.get_text(strip=True).strip('()')
            else:
                details['year'] = '未知'
            
            # 获取类型
            genres = []
            genre_elements = soup.find_all('span', property='v:genre')
            for genre in genre_elements:
                genres.append(genre.get_text(strip=True))
            if genres:
                details['genres'] = ', '.join(genres)
            else:
                details['genres'] = '未知'
            
            # 获取片长
            runtime_element = soup.find('span', property='v:runtime')
            if runtime_element:
                details['runtime'] = runtime_element.get_text(strip=True)
            else:
                details['runtime'] = '未知'
            
            # 获取语言
            language = '未知'
            # 查找包含语言信息的元素
            info_elements = soup.find_all('div', class_='info')
            for info in info_elements:
                text = info.get_text()
                if '语言:' in text or '语言：' in text:
                    lang_match = re.search(r'语言[：:]\s*([^\n]+)', text)
                    if lang_match:
                        language = lang_match.group(1).strip()
                        break
            
            # 如果没有找到语言信息，尝试其他方式
            if language == '未知':
                # 查找所有可能包含语言信息的文本
                all_text = soup.get_text()
                lang_patterns = [
                    r'语言[：:]\s*([^\n\r]+)',
                    r'语言[：:]\s*([^，。\n\r]+)',
                    r'语言[：:]\s*([^，。\s\n\r]+)'
                ]
                
                for pattern in lang_patterns:
                    lang_match = re.search(pattern, all_text)
                    if lang_match:
                        language = lang_match.group(1).strip()
                        break
            
            details['language'] = language
            
            # 获取上映日期
            release_date = '未知'
            release_element = soup.find('span', property='v:initialReleaseDate')
            if release_element:
                release_date = release_element.get_text(strip=True)
            else:
                # 尝试查找其他上映日期信息
                date_patterns = [
                    r'上映日期[：:]\s*([^\n\r]+)',
                    r'上映时间[：:]\s*([^\n\r]+)',
                    r'上映[：:]\s*([^\n\r]+)'
                ]
                
                for pattern in date_patterns:
                    date_match = re.search(pattern, all_text)
                    if date_match:
                        release_date = date_match.group(1).strip()
                        break
            
            details['release_date'] = release_date
            
            print(f"《{movie_name}》信息获取完成")
            return details
            
        except Exception as e:
            print(f"获取《{movie_name}》详细信息时出错: {e}")
            return {}
    
    def save_results(self, movies, base_filename='douban_detailed_ranking'):
        """保存结果到文件"""
        
        # 保存为JSON
        json_filename = f"{base_filename}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(movies, f, ensure_ascii=False, indent=2)
        print(f"JSON文件已保存: {json_filename}")
        
        # 保存为CSV
        csv_filename = f"{base_filename}.csv"
        with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'rank', 'movie_name', 'movie_id', 'movie_url', 
                'rating', 'director', 'actors', 'year', 'genres', 
                'runtime', 'language', 'release_date'
            ])
            writer.writeheader()
            for movie in movies:
                writer.writerow(movie)
        print(f"CSV文件已保存: {csv_filename}")
    
    def run(self):
        """运行爬虫"""
        print("=== 豆瓣电影一周口碑榜详细爬虫 ===")
        print("开始爬取...")
        
        # 获取榜单
        movies = self.get_weekly_ranking()
        
        if not movies:
            print("未获取到电影榜单")
            return
        
        print(f"\n成功获取 {len(movies)} 部电影的基本信息")
        
        # 获取每部电影的详细信息
        print("\n正在获取电影详细信息...")
        for i, movie in enumerate(movies):
            print(f"\n处理第 {i+1}/{len(movies)} 部电影: {movie['movie_name']}")
            
            if movie['movie_id']:
                details = self.get_movie_details(movie['movie_id'], movie['movie_name'])
                movie.update(details)
            
            # 添加延时避免被封
            time.sleep(2)
        
        # 保存结果
        self.save_results(movies)
        
        # 显示结果
        print("\n" + "="*80)
        print("=== 豆瓣电影一周口碑榜详细信息 ===")
        print("="*80)
        
        for movie in movies:
            print(f"\n第{movie['rank']}名: {movie['movie_name']}")
            print(f"豆瓣评分: {movie.get('rating', '未知')}")
            print(f"导演: {movie.get('director', '未知')}")
            print(f"主演: {movie.get('actors', '未知')}")
            print(f"年份: {movie.get('year', '未知')}")
            print(f"类型: {movie.get('genres', '未知')}")
            print(f"片长: {movie.get('runtime', '未知')}")
            print(f"语言: {movie.get('language', '未知')}")
            print(f"上映日期: {movie.get('release_date', '未知')}")
            print(f"豆瓣链接: {movie['movie_url']}")
            print("-" * 80)
        
        print(f"\n总共处理了 {len(movies)} 部电影")

if __name__ == "__main__":
    scraper = DoubanDetailedScraper()
    scraper.run()

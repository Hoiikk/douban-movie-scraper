# 豆瓣电影一周口碑榜爬虫

## 📁 项目文件

- `douban_detailed_scraper.py` - 主要爬虫程序，获取电影详细信息
- `douban_movies_summary.md` - 电影信息汇总文档
- `douban_detailed_ranking.csv` - 爬取数据的CSV格式文件

## 🚀 使用方法

### 运行爬虫
```bash
cd douban
python douban_detailed_scraper.py
```

### 功能特点
- 自动爬取豆瓣电影一周口碑榜前10名
- 获取电影详细信息：语言、主演、上映日期、片长、豆瓣评分
- 支持JSON和CSV格式输出
- 智能解析网页结构，多种备选方案

## 📊 输出结果

爬虫会生成以下文件：
- `douban_detailed_ranking.json` - JSON格式的完整数据
- `douban_detailed_ranking.csv` - CSV格式的完整数据

## 🎯 爬取示例

最新的一周口碑榜前3名：
1. **初吻** (8.5分) - 日语爱情奇幻片
2. **夜班** (8.3分) - 多语言剧情片  
3. **南京照相馆** (8.7分) - 国产历史战争片

## ⚠️ 注意事项

- 确保网络连接正常
- 遵守豆瓣网站的使用条款
- 建议在爬取时添加适当延时
- 仅供学习和研究使用

## 🔧 依赖安装

```bash
pip install requests beautifulsoup4 lxml
```

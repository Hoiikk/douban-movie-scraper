# 🎬 豆瓣电影一周口碑榜爬虫

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Hoiikk/douban-movie-scraper.svg)](https://github.com/Hoiikk/douban-movie-scraper/stargazers)
[![GitHub forks](https://img.shields.io/badge/GitHub-forks-blue.svg)](https://github.com/Hoiikk/douban-movie-scraper/network)

> 一个智能的豆瓣电影爬虫，自动获取豆瓣电影一周口碑榜前10名电影的详细信息，包括语言、主演、上映日期、片长和豆瓣评分等。

## ✨ 功能特点

- 🚀 **自动爬取** - 一键获取豆瓣电影一周口碑榜前10名
- 📊 **详细信息** - 包含语言、主演、上映日期、片长、豆瓣评分等
- 🔄 **智能解析** - 多种解析策略，确保数据完整性
- 📁 **多格式输出** - 支持JSON和CSV格式
- 🛡️ **反爬虫** - 智能请求头伪装，避免被封
- 📈 **实时数据** - 获取最新的电影排名和评分

## 🎯 爬取示例

### 最新一周口碑榜前3名

| 排名 | 电影名称 | 评分 | 类型 | 语言 |
|------|----------|------|------|------|
| 🥇 | 初吻 | 8.5 | 爱情, 奇幻 | 日语 |
| 🥈 | 夜班 | 8.3 | 剧情 | 德语/土耳其语/法语 |
| 🥉 | 南京照相馆 | 8.7 | 剧情, 历史, 战争 | 汉语普通话/日语/南京话 |

## 🚀 快速开始

### 环境要求

- Python 3.7+
- 网络连接

### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/Hoiikk/douban-movie-scraper.git
cd douban-movie-scraper

# 安装依赖包
pip install -r requirements.txt
```

### 使用方法

```bash
# 运行爬虫
python douban_detailed_scraper.py
```

## 📁 项目结构

```
douban-movie-scraper/
├── douban_detailed_scraper.py    # 主要爬虫程序
├── requirements.txt               # Python依赖包
├── .gitignore                    # Git忽略文件
└── README.md                     # 项目说明文档
```

## 📊 输出结果

### 生成文件

- `douban_detailed_ranking.json` - JSON格式的完整数据
- `douban_detailed_ranking.csv` - CSV格式的完整数据

### 数据字段

| 字段 | 说明 | 示例 |
|------|------|------|
| rank | 排名 | 1, 2, 3... |
| movie_name | 电影名称 | 初吻, 夜班... |
| rating | 豆瓣评分 | 8.5, 8.3... |
| director | 导演 | 冢原亚由子... |
| actors | 主演 | 松隆子, 松村北斗... |
| year | 年份 | 2025, 2024... |
| genres | 类型 | 爱情, 奇幻... |
| runtime | 片长 | 124分钟... |
| language | 语言 | 日语, 汉语普通话... |
| release_date | 上映日期 | 2025(中国大陆)... |

## 🔧 技术实现

### 核心技术

- **requests** - HTTP请求库
- **BeautifulSoup4** - HTML解析库
- **lxml** - XML/HTML解析器
- **正则表达式** - 数据提取和清理

### 解析策略

1. **表格解析** - 优先查找HTML表格结构
2. **区域解析** - 查找包含榜单的文本区域
3. **链接搜索** - 直接搜索页面中的电影链接
4. **模式匹配** - 使用正则表达式匹配排名模式

### 反爬虫措施

- 设置真实的User-Agent
- 添加完整的请求头信息
- 合理的请求延时
- 错误重试机制

## 📈 使用统计

- **支持电影数量**: 10部/次
- **数据字段**: 10个
- **输出格式**: 2种 (JSON/CSV)
- **更新频率**: 实时

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 贡献步骤

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 更新日志

### [v1.0.0] - 2025-01-XX
- ✨ 初始版本发布
- 🎯 支持豆瓣电影一周口碑榜爬取
- 📊 获取电影详细信息
- 🔄 多种解析策略
- 📁 多格式输出支持

## ⚠️ 注意事项

- 🚫 **仅供学习研究** - 请勿用于商业用途
- 🌐 **遵守网站规则** - 遵守豆瓣网站的使用条款
- ⏱️ **合理使用频率** - 建议添加适当延时
- 📧 **联系网站** - 如有问题请联系豆瓣官方

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- 感谢豆瓣电影提供数据源
- 感谢开源社区的支持
- 感谢所有贡献者的帮助

## 📞 联系方式

- **GitHub**: [@Hoiikk](https://github.com/Hoiikk)
- **项目地址**: [douban-movie-scraper](https://github.com/Hoiikk/douban-movie-scraper)

---

<div align="center">

**如果这个项目对你有帮助，请给它一个 ⭐ Star！**

Made with ❤️ by [Hoiikk](https://github.com/Hoiikk)

</div>

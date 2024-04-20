import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_article_data(url):
    # Webページを取得
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # スクレイピング対象データの初期化
    articles = []

    # 各記事の情報を抽出
    for article in soup.find_all('div', class_='article-item'):  # 記事を囲む要素とそのクラス名
        title = article.find('h2', class_='title').text  # タイトル
        category = article.find('span', class_='category').text  # カテゴリ
        price = article.find('span', class_='price').text  # 販売価格
        sales = article.find('span', class_='sales').text  # 販売数
        publish_date = article.find('span', class_='publish-date').text  # 公開日
        word_count = article.find('span', class_='word-count').text  # 文字数
        summary = article.find('p', class_='summary').text  # 概要
        author = article.find('span', class_='author').text  # 著者名
        author_profile = article.find('div', class_='author-profile').text  # 著者プロフィール
        
        # 記事情報を辞書に格納し、リストに追加
        articles.append({
            'Title': title,
            'Category': category,
            'Price': price,
            'Sales': sales,
            'Publish Date': publish_date,
            'Word Count': word_count,
            'Summary': summary,
            'Author': author,
            'Author Profile': author_profile
        })

    return articles

# スクレイピングするWebサイトのURL
url = 'https://example.com/articles'

# スクレイピング実行
articles_data = scrape_article_data(url)

# データをDataFrameに変換
df = pd.DataFrame(articles_data)

# Excelファイルとして保存
df.to_excel('articles_data.xlsx', index=False)

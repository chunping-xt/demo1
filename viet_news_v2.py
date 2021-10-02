#python.exe -m pip install --upgrade pip
#pip install feedparser
#pip install newspaper3k
#pip install streamlit

# streamlit run <app.py> for one app
# python run_all.py <folder_path> for multiple apps


import streamlit as st
import feedparser
from urllib.parse import quote
import streamlit.state as state


st.set_page_config(layout="wide")
#st.markdown("<h2 style='text-align: center; font-family: Verdana; color: red;'>Tin tức tổng hợp 24h qua</h2><br>", unsafe_allow_html=True)
#st.markdown("<h4 style='text-align: center;'>Tìm kiếm theo từ khóa hoặc tên báo (ví dụ: Hà Nội, Vaccine, Mạng xã hội, Trí tuệ nhân tạo, cafebiz.vn, Mỹ...)</h4><br>", unsafe_allow_html=True)
#-----------------------------------------------------------------------------------
# Báo tiếng Việt
#-----------------------------------------------------------------------------------
st.sidebar.title("Báo tiếng Việt")
# Custom keywords
keyword = st.sidebar.text_input("Nhập/Xóa từ  khóa", "Hà Nội")

# Select websites
list = ['cafebiz.vn', 'cafef.vn', 'thanhnien.vn','vnexpress.net','soha.vn','zingnews.vn','tuoitre.vn','laodong.vn', 'All']
domain = st.sidebar.multiselect("Chọn websites:",list,default=["All"])

sites = ""
if "All" in domain:
	domain = ""
if domain:
	for i in domain[:-1]:
		sites = sites + "site:{} OR ".format(i)
	sites = sites + "site:" + domain[-1]

query = keyword + " " + sites + " "

if keyword == "" and sites == "":
	query = "Hà Nội"

#st.sidebar.write(query)



#-----------------------------------------------------------------------------------
if st.sidebar.button('Tìm kiếm 🔎'):
	
	url = 'https://news.google.com/rss/search?q=' + quote(query) + 'when:1d&hl=vi' 
	#st.sidebar.write(url)

	feed = feedparser.parse(url)

	i = 1
	html = ""
	for post in feed.entries:

		html = html + f"{post.title[:120]} &nbsp;<a href='{post.link}' target='_blank' > Link </a><br>" 


		if (i % 5 == 0):
			html = html + "<br>"
		i = i+1

	html1 = f"""
			<p style='font-size: 17px; font-family: Segoe UI;color:#202124'> 
				{html} 
			</p>
			"""
	st.markdown("<h2 style='text-align: center; font-family: Verdana; color: red;'>Tin tức 24h</h2><br>", unsafe_allow_html=True)	
	st.markdown(html1, unsafe_allow_html=True)
	
	

#-----------------------------------------------------------------------------------
# Báo tiếng Anh
#-----------------------------------------------------------------------------------
st.sidebar.write("-------------------------------")
st.sidebar.title("English News")
# Custom keywords
keyword_en = st.sidebar.text_input("Input/Delete keyword", "AI")

# Select websites
list_en = ['bbc.com','martechseries.com','analyticsindiamag.com','bloomberg.com', 'cnn.com','cnbc.com','reuters.com','foxnews.com','.entrepreneur.com','techradar.com', 'All']
domain_en = st.sidebar.multiselect("Select websites:",list_en,default=["All"])

sites_en = ""
if "All" in domain_en:
	domain_en = ""
if domain_en:
	for i in domain[:-1]:
		sites_en = sites_en + "site:{} OR ".format(i)
	sites_en = sites_en + "site:" + domain_en[-1]

query_en = keyword_en + " " + sites_en + " "

if keyword_en == "" and sites_en == "":
	query = "Vaccine"

#-----------------------------------------------------------------------------------
if st.sidebar.button('Search 🔎'):
	
	url_en = 'https://news.google.com/rss/search?q=' + quote(query_en) + 'when:1d&hl=en&gl=US' 
	#st.sidebar.write(url)

	feed_en = feedparser.parse(url_en)

	i = 1
	html = ""
	for post_en in feed_en.entries:

		html = html + f"{post_en.title[:120]} &nbsp;<a href='{post_en.link}' target='_blank' > Link </a><br>" 


		if (i % 5 == 0):
			html = html + "<br>"
		i = i+1

	html1 = f"""
			<p style='font-size: 17px; font-family: Segoe UI;color:#202124'> 
				{html} 
			</p>
			"""
	st.markdown("<h2 style='text-align: center; font-family: Verdana; color: red;'>News 24h</h2><br>", unsafe_allow_html=True)	
	st.markdown(html1, unsafe_allow_html=True)
	
	
	#st.sidebar.title(url_en)
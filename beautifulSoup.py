import bs4, requests

def getBbcHeadline(productURL):

    res = requests.get(productURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body div#root div.css-1640cv5-SectionWrapper.eustbbg0 main#main-content.css-f1h9ew-MainSection.eustbbg2 div.css-6gq9s0-Wrap.e42f8510 div.css-16rg7hm-ContainerWithSidebarWrapper.e1jl38b40 div.css-rgov1k-MainColumn.e1sbfw0p0 article.css-i49gvv-ArticleWrapper.e1nh2i2l0 header.css-94m6rd-HeadingWrapper.e1nh2i2l1 h1#main-heading.css-1c1994u-StyledHeading.e1fj1fc10')
    return elems[0].text.strip()

headline = getBbcHeadline('https://www.bbc.co.uk/news/business-54777006')
print('The headline is ' + headline)
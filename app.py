import streamlit as st
from news_fetcher import get_news
from summarizer import summarize_article
from datetime import datetime


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="News Research Tool",
    page_icon="📰",
    layout="wide"
)


# ==================================================
# LOGIN CREDENTIALS
# ==================================================

USERNAME = "admin"
PASSWORD = "admin123"


# ==================================================
# SESSION STATE
# ==================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "search_history" not in st.session_state:
    st.session_state.search_history = []

if "articles" not in st.session_state:
    st.session_state.articles = []

if "current_query" not in st.session_state:
    st.session_state.current_query = ""

if "saved_articles" not in st.session_state:
    st.session_state.saved_articles = {}

if "total_searches" not in st.session_state:
    st.session_state.total_searches = 0


# ==================================================
# LOGIN PAGE
# ==================================================

if not st.session_state.logged_in:

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #f7f9fc;
        }

        .login-title {
            text-align: center;
            font-size: 44px;
            font-weight: 700;
            color: #163b65;
            margin-top: 70px;
        }

        .login-subtitle {
            text-align: center;
            font-size: 17px;
            color: #64748b;
            margin-bottom: 35px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-title">'
        '📰 News Research Tool'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="login-subtitle">'
        '🔐 Secure Login to Continue'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        username = st.text_input(
            "👤 Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "🔑 Password",
            type="password",
            placeholder="Enter password"
        )

        login_button = st.button(
            "🔐 Login",
            use_container_width=True
        )

        if login_button:

            if (
                username.strip() == USERNAME
                and password == PASSWORD
            ):

                st.session_state.logged_in = True

                st.success(
                    "✅ Login successful!"
                )

                st.rerun()

            else:

                st.error(
                    "❌ Invalid username or password."
                )

    st.stop()


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f7f9fc;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #163b65;
        margin-bottom: 3px;
    }

    .subtitle {
        font-size: 17px;
        color: #64748b;
        margin-bottom: 20px;
    }

    .header-line {
        height: 3px;
        background-color: #163b65;
        border-radius: 5px;
        margin-bottom: 25px;
    }

    .stat-card {
        background-color: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        text-align: center;
        min-height: 110px;
    }

    .stat-title {
        font-size: 14px;
        color: #64748b;
        margin-bottom: 8px;
    }

    .stat-value {
        font-size: 25px;
        font-weight: 700;
        color: #163b65;
    }

    .search-heading {
        font-size: 20px;
        font-weight: 700;
        color: #163b65;
        margin-bottom: 8px;
    }

    .article-title {
        font-size: 23px;
        font-weight: 700;
        color: #163b65;
        line-height: 1.4;
        margin-top: 10px;
        margin-bottom: 12px;
    }

    .summary-title {
        font-size: 17px;
        font-weight: 700;
        color: #222222;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .summary-text {
        font-size: 16px;
        line-height: 1.7;
        color: #444444;
    }

    .metadata {
        font-size: 14px;
        color: #64748b;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #163b65;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================

header_col1, header_col2 = st.columns([6, 1])

with header_col1:

    st.markdown(
        '<div class="main-title">'
        '📰 News Research Tool'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Search the latest news and get instant article summaries.'
        '</div>',
        unsafe_allow_html=True
    )

with header_col2:

    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.articles = []
        st.rerun()


st.markdown(
    '<div class="header-line"></div>',
    unsafe_allow_html=True
)


# ==================================================
# DASHBOARD STATISTICS
# ==================================================

article_count = len(
    st.session_state.articles
)

current_topic = (
    st.session_state.current_query
    if st.session_state.current_query
    else "None"
)

stat1, stat2, stat3 = st.columns(3)

with stat1:

    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-title">
                📰 Articles Found
            </div>
            <div class="stat-value">
                {article_count}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat2:

    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-title">
                🔎 Current Topic
            </div>
            <div class="stat-value">
                {current_topic}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat3:

    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-title">
                🔐 User Status
            </div>
            <div class="stat-value">
                Logged In
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("")


# ==================================================
# SEARCH SECTION
# ==================================================

st.markdown(
    '<div class="search-heading">'
    '🔎 Search Any News Topic'
    '</div>',
    unsafe_allow_html=True
)

search_col1, search_col2 = st.columns([5, 1])

with search_col1:

    query = st.text_input(
        "News Topic",
        placeholder=(
            "Artificial Intelligence, Cricket, "
            "Bollywood, Pune, ISRO, Tesla, Jobs..."
        ),
        label_visibility="collapsed"
    )

with search_col2:

    search_button = st.button(
        "🔍 Search",
        use_container_width=True
    )


# ==================================================
# RECENT SEARCHES
# ==================================================

st.markdown(
    '<div class="section-title">'
    '🕒 Recent Searches'
    '</div>',
    unsafe_allow_html=True
)

if st.session_state.search_history:

    recent_searches = (
        st.session_state.search_history[-5:][::-1]
    )

    history_columns = st.columns(
        len(recent_searches)
    )

    for index, search in enumerate(
        recent_searches
    ):

        with history_columns[index]:

            if st.button(
                f"🔎 {search}",
                key=f"recent_{index}_{search}",
                use_container_width=True
            ):

                st.session_state.selected_search = search
                st.rerun()

else:

    st.caption(
        "No recent searches yet. Search for a topic to get started."
    )


# ==================================================
# HANDLE RECENT SEARCH
# ==================================================

if "selected_search" in st.session_state:

    selected_search = (
        st.session_state.selected_search
    )

    del st.session_state.selected_search

    query = selected_search
    search_button = True


# ==================================================
# FETCH NEWS
# ==================================================

if search_button:

    if not query.strip():

        st.warning(
            "⚠️ Please enter a news topic to search."
        )

        st.stop()


    # Count search
    st.session_state.total_searches += 1


    # Save search history
    if query not in st.session_state.search_history:

        st.session_state.search_history.append(
            query
        )


    # Keep last 10 searches
    st.session_state.search_history = (
        st.session_state.search_history[-10:]
    )


    # Fetch news
    with st.spinner(
        "🔄 Fetching latest news..."
    ):

        try:

            articles = get_news(query)

        except Exception as e:

            st.error(
                "❌ Error while fetching news."
            )

            st.error(str(e))

            st.stop()


    # No articles
    if not articles:

        st.error(
            "❌ No news articles found for this topic."
        )

        st.stop()


    # Store articles
    st.session_state.articles = articles
    st.session_state.current_query = query

    st.rerun()


# ==================================================
# DISPLAY ARTICLES
# ==================================================

if st.session_state.articles:

    articles = st.session_state.articles

    current_query = (
        st.session_state.current_query
    )


    st.success(
        f"✅ Found {len(articles)} articles for "
        f"**{current_query}**"
    )


    st.markdown(
        '<div class="section-title">'
        '📰 Latest News'
        '</div>',
        unsafe_allow_html=True
    )


    # ==================================================
    # EACH ARTICLE
    # ==================================================

    for i, article in enumerate(
        articles,
        start=1
    ):

        title = article.get(
            "title",
            "No title available"
        )

        source_data = article.get(
            "source",
            {}
        )

        source = source_data.get(
            "name",
            "Unknown"
        )

        published = article.get(
            "publishedAt",
            "Unknown"
        )

        url = article.get(
            "url",
            ""
        )

        image_url = article.get(
            "urlToImage",
            ""
        )


        # ==================================================
        # DATE FORMAT
        # ==================================================

        formatted_date = published

        try:

            date_obj = datetime.fromisoformat(
                published.replace(
                    "Z",
                    "+00:00"
                )
            )

            formatted_date = date_obj.strftime(
                "%d %B %Y, %I:%M %p"
            )

        except (
            ValueError,
            AttributeError
        ):

            formatted_date = published


        # ==================================================
        # ARTICLE CARD
        # ==================================================

        with st.container(border=True):

            # Article image
            if image_url:

                try:

                    image_col1, image_col2, image_col3 = (
                        st.columns([1, 3, 1])
                    )

                    with image_col2:

                        st.image(
                            image_url,
                            width=650
                        )

                except Exception:

                    pass


            # Article title
            st.markdown(
                f'<div class="article-title">'
                f'{i}. {title}'
                f'</div>',
                unsafe_allow_html=True
            )


            # Summary heading
            st.markdown(
                '<div class="summary-title">'
                '📝 Article Summary'
                '</div>',
                unsafe_allow_html=True
            )


            # Generate summary
            with st.spinner(
                f"Preparing summary for article {i}..."
            ):

                try:

                    summary = summarize_article(
                        article
                    )

                except Exception:

                    summary = article.get(
                        "description",
                        "No description available "
                        "for this article."
                    )


            # Summary
            st.markdown(
                f'<div class="summary-text">'
                f'{summary}'
                f'</div>',
                unsafe_allow_html=True
            )


            # Metadata
            st.markdown(
                f'<div class="metadata">'
                f'📰 <b>Source:</b> {source}'
                f'&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;'
                f'📅 <b>Published:</b> {formatted_date}'
                f'</div>',
                unsafe_allow_html=True
            )


            # Read article
            if url:

                st.link_button(
                    "🔗 Read Full Article",
                    url
                )


            # ==================================================
            # SAVE ARTICLE
            # ==================================================

            article_key = url if url else title

            if article_key in st.session_state.saved_articles:

                st.success(
                    "🔖 Article Saved"
                )

            else:

                if st.button(
                    "🔖 Save Article",
                    key=f"save_article_{i}_{article_key}"
                ):

                    st.session_state.saved_articles[
                        article_key
                    ] = article

                    st.success(
                        "✅ Article saved successfully!"
                    )

                    st.rerun()


# ==================================================
# EXTENDED FEATURES
# ==================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">'
    '🚀 Extended Features'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# SEARCH STATISTICS
# ==================================================

stat_col1, stat_col2, stat_col3 = st.columns(3)

with stat_col1:

    st.metric(
        "🔎 Total Searches",
        st.session_state.total_searches
    )

with stat_col2:

    st.metric(
        "🕒 History Items",
        len(st.session_state.search_history)
    )

with stat_col3:

    st.metric(
        "🔖 Saved Articles",
        len(st.session_state.saved_articles)
    )


# ==================================================
# EXPORT SUMMARIES
# ==================================================

if st.session_state.articles:

    st.markdown(
        "### 📥 Export Current News Summaries"
    )

    export_text = ""

    export_text += (
        "NEWS RESEARCH TOOL\n"
    )

    export_text += (
        "==============================\n\n"
    )

    export_text += (
        f"Search Topic: "
        f"{st.session_state.current_query}\n\n"
    )


    for i, article in enumerate(
        st.session_state.articles,
        start=1
    ):

        title = article.get(
            "title",
            "No title available"
        )

        source_data = article.get(
            "source",
            {}
        )

        source = source_data.get(
            "name",
            "Unknown"
        )

        published = article.get(
            "publishedAt",
            "Unknown"
        )

        url = article.get(
            "url",
            ""
        )


        try:

            summary = summarize_article(
                article
            )

        except Exception:

            summary = article.get(
                "description",
                "No description available."
            )


        export_text += (
            f"{i}. {title}\n"
        )

        export_text += (
            f"Source: {source}\n"
        )

        export_text += (
            f"Published: {published}\n"
        )

        export_text += (
            f"Summary: {summary}\n"
        )

        export_text += (
            f"Article URL: {url}\n"
        )

        export_text += (
            "\n------------------------------\n\n"
        )


    st.download_button(
        label="📥 Download Summaries as TXT",
        data=export_text,
        file_name="news_summaries.txt",
        mime="text/plain",
        use_container_width=True
    )


# ==================================================
# SAVED ARTICLES
# ==================================================

st.markdown("### 🔖 Saved Articles")

if st.session_state.saved_articles:

    for index, (
        key,
        article
    ) in enumerate(
        st.session_state.saved_articles.items(),
        start=1
    ):

        saved_title = article.get(
            "title",
            "No title available"
        )

        saved_source_data = article.get(
            "source",
            {}
        )

        saved_source = saved_source_data.get(
            "name",
            "Unknown"
        )

        saved_url = article.get(
            "url",
            ""
        )


        with st.container(border=True):

            st.markdown(
                f"**{index}. {saved_title}**"
            )

            st.caption(
                f"📰 Source: {saved_source}"
            )

            if saved_url:

                st.link_button(
                    "🔗 Open Saved Article",
                    saved_url
                )

else:

    st.info(
        "🔖 No saved articles yet. "
        "Click 'Save Article' on any news article."
    )


# ==================================================
# SEARCH HISTORY
# ==================================================

st.markdown("### 🕘 Search History")

if st.session_state.search_history:

    for index, search in enumerate(
        st.session_state.search_history[::-1],
        start=1
    ):

        st.write(
            f"**{index}.** 🔎 {search}"
        )

else:

    st.info(
        "No search history available yet."
    )
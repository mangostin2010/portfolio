import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title='강예건의 포트폴리오', page_icon='😀', layout='centered')

# style.css 파일 불러옴
with open('style.css', encoding='UTF-8') as f: st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)


add_vertical_space(2)

with stylable_container(
    key='image',
    css_styles="""
        {
            img {
                display: block;
                object-fit: cover;
                border-radius: 4px;
                width: 124.32px;
                height: 124.32px;
                transition: opacity 100ms ease-out 0s;
                transform: rotate(90deg);
            }
        }
        """,
):
    st.image('files/20240130_122143.jpg')

st.title('강예건의 포트폴리오')


'#### 안녕하세요, IT서비스를 만드는 강예건이라고 합니다.'
with st.container():
    st.write(f'**{open("introduce.txt", encoding="UTF-8").read()}**')

add_vertical_space(3)
col1, col2 = st.columns(2)
with col1:
    st.subheader('👦 Profile', divider='gray')

    '👼  2010년 9월 12일 출생'
    '👶  수원어린이집 졸업'
    '🏫  수원기독국제학교(SCIS) 재학중'



with col2:
    st.subheader('💡 Contact', divider='gray')

    '📭  scisjustin@gmail.com'
    '📞  010-5746-5920'
    '📸  [@yg201009](https://www.instagram.com/yg201009)'


add_vertical_space(3)
col1, col2 = st.columns(2)
with col1:
    st.subheader('📝 Blog', divider='gray')
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: 0.3rem 1rem 1rem 1rem;
            }
            """,
    ):
        '#### Bloggie'
        '(현재 호스팅 되지 않을 수 있음)'
        'http://bloggie.kro.kr'
        '#####'

with col2:
    st.subheader('🗃 Github', divider='gray')
    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: 0.3rem 1rem 1rem 1rem;
            }
            """,
    ):
        '#### Mangostin2010'
        'https://github.com/mangostin2010'
        '#####'
        '###'

add_vertical_space(3)
with st.container():
    st.subheader('⚒  Personal Project', divider='gray')
    col1, col2 = st.columns(2)
    with col1:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: 0.3rem 1rem 1rem 1rem;
                }
                """,
        ):
            '#### Illuda(일루다)👧'
            'https://github.com/mangostin2010/Illuda'
            'https://illuda.streamlit.app'
            '#####'
    with col2:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: 0.3rem 1rem 1rem 1rem;
                }
                """,
        ):
            '#### AI-Toron🤖'
            'https://github.com/mangostin2010/AI-Toron'
            'https://aitoron.streamlit.app'
            '#####'



    col1, col2 = st.columns(2)
    with col1:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: 0.3rem 1rem 1rem 1rem;
                }
                """,
        ):
            '#### Weather🌨️'
            'https://github.com/mangostin2010/Weather'
            'https://weather4korea.streamlit.app'
            '#####'
    with col2:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: 0.3rem 1rem 1rem 1rem;
                }
                """,
        ):
            '#### Word-Wise🤓'
            'https://github.com/mangostin2010/Word-Wise'
            'https://word-wise.streamlit.app/'
            '#####'
            

    col1, col2 = st.columns(2)
    with col1:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: 0.3rem 1rem 1rem 1rem;
                }
                """,
        ):
            '#### Bloggie📚'
            '(현재 호스팅 되지 않을 수 있음)'
            'http://bloggie.kro.kr'
            '####'
            '######'
    with col2:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: 0.3rem 1rem 1rem 1rem;
                }
                """,
        ):
            '#### literary-style-changer'
            'https://bit.ly/literary-style-changer'
            '(현재 호스팅 되지 않을 수 있음)'
            'http://bloggie.kro.kr:8501'
            '#####'

    col1, col2 = st.columns(2)
    with col1:
        with stylable_container(
            key="container_with_border",
            css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 0.5rem;
                    padding: 0.3rem 1rem 1rem 1rem;
                }
                """,
        ):
            '#### KKaetalk깨톡🗨️'
            '(현재 호스팅 되지 않을 수 있음)http://kkaetalk.kro.kr'
            '#####'

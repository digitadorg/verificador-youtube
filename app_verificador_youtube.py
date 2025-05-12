import streamlit as st

st.set_page_config(page_title="Detector de Anúncios no YouTube", page_icon="🎯")

st.title("🎯 Detector de Anúncios no YouTube")
st.markdown("Este app ajuda você a **verificar se um vídeo do YouTube exibe anúncios** e pode ser segmentado no Google Ads.")

st.markdown("### 🚀 Como funciona?")
st.markdown("""
1. Copie e cole o link de um vídeo do YouTube abaixo.
2. O sistema **orienta como verificar anúncios** manualmente (por enquanto).
3. A versão automatizada será integrada com robô Selenium e navegador headless.
""")

video_url = st.text_input("🔗 Cole o link do vídeo do YouTube aqui:")

if video_url:
    st.markdown("### 🧪 Teste manual sugerido:")
    st.markdown(f"- Abra o vídeo: [Clique aqui]({video_url})")
    st.markdown("- Desative bloqueadores de anúncios")
    st.markdown("- Veja se aparece algum dos seguintes:")
    st.markdown("  - Anúncio em vídeo (antes, durante ou depois)")
    st.markdown("  - Banner sobreposto com botão de fechar")
    st.markdown("  - Botão 'Pular anúncio'")

    st.info("Se algum dos elementos aparecer, o vídeo está monetizado e aceita anúncios.")

st.markdown("---")
st.markdown("🔒 *Este app não coleta dados. Apenas fornece instruções para verificação manual.*")

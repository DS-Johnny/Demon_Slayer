import pandas as pd
import streamlit as st
from PIL import Image


arquivo = pd.read_csv('characters.csv')
df = pd.DataFrame(arquivo)
df.fillna('-', inplace=True)
ds = df[df['Category'] == 'Demon Slayer']



# --------------------------------------------SIDEBAR
st.sidebar.title('Demon Slayers')
nomes = ds['Character Name'].unique()

personagem = st.sidebar.selectbox('Personagens:', nomes)



#----------------------------------------------BODY
st.title(personagem)

imagem = f'{personagem}.png'
image = Image.open(imagem)
st.image(image, width=300)

st.markdown("""---""")

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.write('Raça:')
        raca = ds[ds['Character Name'] == personagem]['Race'].tolist()
        st.write(raca[0])

    
    with col2:
        st.write('Gênero:')
        gen = ds[ds['Character Name'] == personagem]['Gender'].tolist()
        st.write(gen[0])

        
    
    with col3:
        st.write('Idade:')
        idade = ds[ds['Character Name'] == personagem]['Age'].tolist()
        st.write(str(idade[0]))

    
    
    with col4:
        st.write('Grupo:')
        grupo = ds[ds['Character Name'] == personagem]['Affiliation'].tolist()
        st.write(grupo[0])

    
    with col5:
        st.write('Apelido:')
        apelido = ds[ds['Character Name'] == personagem]['Alias'].tolist()
        st.write(apelido[0])
        
st.markdown("""---""")        
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.write('Habilidades:')
        habilidades = ds[ds['Character Name'] == personagem]['Abilities'].tolist()
        st.write(habilidades[0])
    with col2:
        st.write('Respiração:')
        respiracao = ds[ds['Character Name'] == personagem]['Breathing Style '].tolist()
        st.write(respiracao[0])
    with col3:
        st.write('Estilo de luta:')
        estilo = ds[ds['Character Name'] == personagem]['Fighting Style'].tolist()
        st.write(estilo[0])
    with col4:
        st.write('Kekkijutsu:')
        kekkijutsu = ds[ds['Character Name'] == personagem]['Demon Art'].tolist()
        st.write(kekkijutsu[0])
    with col5:
        st.write('Equipamentos:')
        equips = ds[ds['Character Name'] == personagem]['Equipment'].tolist()
        st.write(equips[0])
st.markdown("""---""")
with st.container():
    st.write('Luta Contra:')
    lutas = ds[ds['Character Name'] == personagem]['Fights'].tolist()
    st.write(lutas[0])
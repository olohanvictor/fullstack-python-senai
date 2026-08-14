import streamlit as st 
import database as db 

db.criar_tabela()

st.title("esse é um titulo")
st.header("esse é um cabeçalho")
st.subheader("esse é um cabeçalho menor")

with st.form("nome_do_formulario"):
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", value = 50)
    nota = st.number_input("Nota", value= 0.0, step= 0.5, min_value= 0.0, max_value= 10.0)


    #cargo = st.text_input("Cargo")
    #dt_nasc = st.date_input("Campo data", value="today")

    btn_form = st.form_submit_button("Enviar")

if btn_form:
    conn = db.conectar() #conecto
    cursor = conn.cursor() #crio o cursor

    cursor.execute("INSERT INTO alunos(nome, idade, nota) VALUES (?, ?, ?)", (nome, idade, nota))

    conn.commit() #commito o que eu fiz
    conn.close() #fecho a conexão
    


#if btn_form:
#    st.write("Seus dados foram enviados com sucesso.")
#    st.write(f"Nome: {nome}")
#    st.write(f"Idade: {idade}")
#    st.write(f"Nota: {nota}")
#    st.write(f"Cargo: {cargo}")
#    st.write(f"Data de nasicmento: {dt_nasc}")
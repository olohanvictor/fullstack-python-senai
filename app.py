import streamlit as st 
import database as db 

db.criar_tabela()

st.title("esse é um titulo")
st.header("esse é um cabeçalho")
st.subheader("esse é um cabeçalho menor")

#Cadastrando a nota dos alunos
with st.form("cadastrar_aluno"):
    nome = st.text_input("Nome")
    idade = st.number_input("Idade", value = 50)
    nota = st.number_input("Nota", value = 0.0, step= 0.5, min_value= 0.0, max_value= 10.0)


    btn_form = st.form_submit_button("Enviar")

#Inserindo dados no banco de dados
if btn_form:
    db.criar_aluno(nome, idade, nota)

    #if btn_form:
#    st.write("Seus dados foram enviados com sucesso.")
#    st.write(f"Nome: {nome}")
#    st.write(f"Idade: {idade}")
#    st.write(f"Nota: {nota}")
#    st.write(f"Cargo: {cargo}")
#    st.write(f"Data de nasicmento: {dt_nasc}")
    
#Procurando alunos
with st.form("buscar_aluno"):
    nome = st.text_input("Nome do aluno")
    btn_buscar = st.form_submit_button("Buscar")

if btn_buscar:

    alunos = db.buscar_aluno(nome)

    if alunos:
        st.dataframe(
            alunos,
            column_config={ #Puramente visual. É o nome que fica em cada campo da tabela
                1: "ID",
                2: "Nome",
                3: "Idade",
                4: "Nota"
            },
            hide_index=True
        )

    else:
        st.write("Nenhum aluno encontrado.")

#Editando alunos
with st.form("editar_aluno"):
    id = st.text_input("ID do Aluno a ser alterado")
    nome = st.text_input("Novo NOME")
    idade = st.number_input("Nova IDADE", value = 50)
    nota = st.number_input("Nova NOTA", value = 0.0, step= 0.5, min_value= 0.0, max_value= 10.0)

    btn_form = st.form_submit_button("Editar")

    if btn_form:
        db.editar_aluno(id, nome, idade, nota)

#Deletando alunos
with st.form("deletar_aluno"):
    id = st.text_input("ID do Aluno a ser deletado")

    btn_form = st.form_submit_button("Deletar")

    if btn_form:
        db.deletar_aluno(id)

# recomendolivros

Projeto desenvolvido para trabalho do terceiro ano do ensino médio (2020) para ser apresentado na MOSTRA SESI cujo o tema era Inteligência Artificial. A problématica apresentada pelo grupo consistia no uso diverso de sistemas de recomendação e sua influência nos usuários. Diante disso, foi emulado um sistema recomendador de livros, utilizando o algoritmo tf-idf (do inglês term frequency–inverse document frequency), com dataset desenvolvido pelos alunos integrantes do grupo.

Bibliotecas utilizadas:
- pandas
- streamlit
- Pillow
- sklearn

Projeto bastante básico, baseado em alguns tutoriais, desenvolvido com pouca experiência nas tecnologias.
Deploy foi realizado na plataforma heroku, onde continua hospedado no endereço: https://recomendolivros.herokuapp.com/

## Run locally:

Clone the proeject:
```console
git clone https://github.com/erarich/recomendolivros.git
```

Enter the project's directory:
```console
cd recomendolivros
```

Create a virtual enviroment:
```console
python -m venv venv/
```

Activate the virtual enviroment:
```console
.\venv\Scripts\Activate.ps1
```

Install dependencies:
```console
pip install -r requirements.txt
```

Start the server:
```console
streamlit run Home.py
```
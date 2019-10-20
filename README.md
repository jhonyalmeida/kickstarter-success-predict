# Kickstarter: previsão de sucesso ou falha da campanha

## Dados da base
- Base Kickstarter
- Fonte: Kaggle
- Link: https://www.kaggle.com/kemical/kickstarter-projects/download
- Descricão: base de campanhas do Kickstarter, coletadas em 2018, com seus respectivos status (sucesso ou fracasso)

## Atributos:
- ID: Contém o ID do projeto
- name : Título do projeto
- category: Subcategoria do projeto (conjunto de valores pré-determinados)
- main_category: Macro-categoria do projeto (conjunto de valores pré-determinados)
- currency: Moeda (local) usada para as doações ao projeto
- launched: Data de início da campanha
- deadline: Data em que se encerra a campanha
- goal: Valor-objetivo para a campanha ter sucesso
- pledged: Valor arrecadado pela campanha
- backers: Número de apoiadores do projeto (ou número estimado, para o caso de previsões)
- country: País da pessoa que está lançando a campanha
- usd pledged: valor da coluna pledged convertida para dólares americanos (conversão feita pelo próprio kickstarter)
- usd_pledged_real: valor da coluna pledged convertida para dólares americanos (conversão feita pela API Fixer.io)
- usd_goal_real: valor da coluna goal convertida para dólares americanos (conversão feita pela API Fixer.io)
- state: Status da campanha, pode assumir os valores: Sucesso, Fracasso, Cancelado, Em Andamento

## Problema:
Prever se a campanha terá ou não sucesso, dados os atributos conhecidos em seu lançamento, como categoria, paiz do lançador da campanha, valor almejado, etc (os registros com estado cancelado ou em andamento serão desconsiderados)

## Como executar e testar:

- Rodar todas as células do jupyter notebook, que contemplam os módulos de treinamento e avaliação 
de três classificadores, selecionando o que obtiver melhor Kappa para gerar o arquivo do modelo que
será utilizado pela aplicação de previsão 

- Rodar a aplicação de inferência, que inicia um servidor Flask local escutando na porta 5000

- Endpoint para simular uma previsão (localmente): POST http://localhost:5000/predict

- Exemplo do JSON da requisição:

```
{
    "main_category": "Fashion",
    "currency": "EUR",
    "goal": 3000,
    "country": "FR",
	"duration_days": 60,
	"backers": 50
}
```

- Para os valores dos atributos main_category, country e currency, usar um dos valores listados 
nos respectivos endpoints: GET /categories, GET /countries e GET /currencies. Os valores também
são listados no notebook para visualização

- Para os valores numéricos, há algum bug que não aceita o valor 0 (parece que o scaler reconhece 
como vazio ao invés do número zero)






# imobpy
APIs Restfull para o ramo imobiliario, calcula preço do imovel a partir da quantidade de metros quadrados

<p>
Para testar localmente em um ambiente com sistema Linux ( substitua python por python3 e pip por pip3 caso seja uma distribuição derivada do ubuntu):
</p>

<pre>
pip install flask
pip install requests
</pre>

<p>
Para executar a API1 (valor do metro fixo):
</p>

<p>
Dentro da pasta desse projeto, digite:
</p>

<pre>
cd API-valormetro

python web.py
</pre>

<p>
Abrir um navegador e acessar http://localhost:5000/valormetro 
</p>

<p>
Para testar a que subi para o heroku troque:
</p>

<p>
http://localhost:5000/valormetro por 
https://imobpy.herokuapp.com/valormetro
</p>

<p>
Para executar a API2 (valor do imovel com a quantidade de metros informados):
</p>

<p>
Deixe executando a API1
</p>

<p>
Em outra janela do terminal, dentro da pasta desse projeto digite:
</p>

<pre>
cd API-valorImovel

python web.py

</pre>

<p>
Abrir um navegador e acessar http://localhost:5001/valorimovel?qtdmetro=10
</p>

<p>
Onde 10 é a quantidade de metros quadrados ( cada metro vale R$ 753,32 )
</p>

<p>
Para testar a que subi para o heroku troque:
</p>


<p>
http://localhost:5001/valorImovel?qtdmetro=10 por 
https://imobpy2.herokuapp.com/valorimovel?qtdmetro=10
</p>

<p>
Para executar os testes instale o pytest com o comando abaixo:
</p>

<pre>
pip install pytest
</pre>

<p>
Caso digite pytest na linha de comando e apresente a mensagem de comando não encontrado, provavelmente ele não foi instalado em uma pasta especifica pela variavel de ambiente $PATH, nesse caso digite:
</p>

<pre>
/home/[seu usuario]/.local/bin/pytest
</pre>

<p>
Os dois arquivos test_web*.py serão executados.
</p>

<p>
Para subir as duas APIs no Heroku:
</p>

<p>
Entre em sua conta do heroku:
</p>

<p>
Em new crie uma nova aplicação de nome api1
</p>

<p>
instale o heroku cli com o comando:
</p>

<pre>
curl https://cli-assets.heroku.com/install.sh | sh
</pre>

<p>
Depois crie uma pasta e entre nela, depois digite os comandos abaixo:
</p>

<pre>
heroku login
</pre>

<p>
Esse comando abrira o navegador padrão para que vc logue em sua conta heroku, apos logar, esse comando finalizara com sucesso.
</p>

<p>
Depois digite o comando:
</p>

<pre>
heroku git:clone -a api1
cd api1
</pre>

<p>
Copie todo o conteudo que está dentro da pasta API-valormetro para essa pasta.
</p>

<pre>
git add .
git commit -am "Coloque um comentario do commit aqui"
git push heroku master
</pre>

<p>
Se der tudo certo, a sua aplicação estara no ar, acesse o link informado no final do processo, geralmente é https://[nome do seu app heroku].herokuapp.com/valormetro
</p>
<br>
<br>
-------------------------
<br>
<br>
 
<p>
Em new crie uma nova aplicação de nome api2
</p>

<p>
Vá na pasta API-valorImovel/config
</p>

<p>
E acesse o arquivo Config.py e mude a url para a url da API1 que está no heroku.
</p>

<p>
Depois crie uma pasta e entre nela, depois digite os comandos abaixo:
</p>

<pre>
heroku login
</pre>

<p>
Esse comando abrira o navegador padrão para que vc logue em sua conta heroku, apos logar, esse comando finalizara com sucesso.
</p>

<p>
Depois digite o comando:
</p>

<pre>
heroku git:clone -a api2
cd api2
</pre>

<p>
Copie todo o conteudo que está dentro da pasta API-valorImovel para essa pasta.
</p>

<pre>
git add .
git commit -am "Coloque um comentario do commit aqui"
git push heroku master
</pre>

<p>
Se der tudo certo, a sua aplicação estara no ar, acesse o link informado no final do processo, geralmente é https://[nome do seu app heroku].herokuapp.com/valorimovel?qtdmetro=10
</p>
<br>
<br>
<p>
Obs: Infelizmente não consegui fazer a integração com o Swagger para facilitar os testes. :-(
</p>

<br>
<br>

-------------------------


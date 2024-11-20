# **Ingestão de Dados em Tempo Real** | Projeto de Engenharia de Dados End-to-End

---

# **Tópicos**

<ol type="1">
  <li>Introdução:;</li>
  <li>Arquitetura do Sistema:;</li>
  <li>Principais pontos abordados na criação do pipeline:;</li>
  <li>Tecnologias utilizadas no projeto:;</li>
</ol>

## 1\. Introdução:

> O objetivo deste projeto é a construção de um pipeline de engenharia de dados end-to-end. Ele cobre cada estágio, desde a ingestão de dados até o processamento e, finalmente, o armazenamento, utilizando um conjunto de tecnologias robustas que inclui Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark e Cassandra. Tudo é containerizado usando Docker para facilitar a implantação e escalabilidade.

## 2\. Arquitetura do Sistema:

![modulo_43-4.png](https://github.com/jaquessonoliveira/Projeto-Ingestao-de-Dados--em-Streaming/blob/main/Arquitetura%20Engenharia%20de%20dados.png)

**O projeto foi desenvolvido com os seguintes componentes:**

- Fonte de Dados: Foi utilizada a API randomuser.me para gerar dados de usuários aleatórios para o pipeline de dados;
- Apache Airflow: Responsável por orquestrar o pipeline e armazenar os dados obtidos em um banco de dados PostgreSQL;
- Apache Kafka e Zookeeper: Usados para transmitir dados do PostgreSQL para o motor de processamento;
- Control Center e Schema Registry: Auxiliam no monitoramento e gerenciamento de esquemas dos fluxos Kafka;
- Apache Spark: Para processamento de dados com seus nós master e worker nodes;
- Cassandra: Onde os dados processados serão armazenados.

## 3\. Principais pontos abordados na criação do pipeline:

- Configuração de um pipeline de dados com Apache Airflow;
- Transmissão de dados em tempo real com Apache Kafka;
- Sincronização distribuída com Apache Zookeeper;
- Técnicas de processamento de dados com Apache Spark;
- Soluções de armazenamento de dados com Cassandra e PostgreSQL;
- Containerização de todo o seu setup de engenharia de dados com Docker.

## 4\. Tecnologias utilizadas no projeto:

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

**Obs:** Os arquivos e códigos utilizados e dezenvolvidos no projeto estão organizados no repositório, assim como o arquivo de configuração "docker-compose".

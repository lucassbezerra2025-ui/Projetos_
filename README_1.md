# 📋 Sistema de Cadastro de Parceiros

Este é um projeto simples em Python que permite cadastrar e buscar oficinas parceiras com base no estado (UF).

---

## 🚀 Funcionalidades

* Cadastro de parceiros (oficinas)
* Armazenamento em memória usando lista
* Busca de parceiros por estado (UF)
* Interface simples via terminal

---

## 🧠 Estrutura do Projeto

O sistema utiliza:

* **Lista (`banco_dados`)** para armazenar os dados
* **Dicionários (`dict`)** para representar cada parceiro
* Funções para organizar as operações

### 📦 Estrutura de dados

Cada parceiro é armazenado no formato:

```python
{
    'Nome': nome,
    'Endereço': end,
    'Telefone': tel,
    'Cidade': cid,
    'Estado': uf
}
```

---

## 🔧 Funções

### ➤ cadastro_parceiro(nome, end, tel, cid, uf)

Responsável por cadastrar uma nova oficina no sistema.

**Parâmetros:**

* `nome`: Nome da oficina
* `end`: Endereço
* `tel`: Telefone
* `cid`: Cidade
* `uf`: Estado

**Retorno:**

* `True` após cadastro bem-sucedido

---

### ➤ buscar_parceiro(uf)

Busca oficinas cadastradas com base no estado informado.

**Parâmetros:**

* `uf`: Sigla do estado

**Retorno:**

* Lista de parceiros encontrados

---

## ▶️ Como usar

1. Execute o script em Python
2. Escolha uma das opções do menu:

```
[1] Cadastro
[2] Buscar
[0] Sair
```

---

### 📌 Cadastro

Informe os dados solicitados:

* Nome
* Endereço
* Telefone
* Cidade
* Estado

---

### 🔍 Busca

Digite a sigla do estado (UF) para listar os parceiros cadastrados.

---

## 💡 Melhorias Futuras

* Salvar dados em arquivo (`.json` ou banco de dados)
* Validação de entrada de dados
* Interface gráfica (GUI)
* pré-definir Estados (Siglas) em um tupla
* Busca por cidade ou nome

---

## 📄 Licença

Este projeto é livre para uso e estudo.

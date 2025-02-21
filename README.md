# 🔐 Sistema de Autenticação em Django

Este é um sistema de autenticação em Django que inclui funcionalidades de **registro, login, logout e envio de e-mails de boas-vindas**. Ele usa autenticação por **e-mail em vez de username**, e os nomes de usuário são gerados automaticamente a partir do nome completo do usuário.

## 📌 Funcionalidades

✅ Registro de novos usuários  
✅ Login e Logout  
✅ Redirecionamento automático após login/logout  
✅ Username gerado automaticamente baseado no nome  
✅ E-mails de boas-vindas com link para login  
✅ Proteção contra usuários duplicados  
✅ Validação avançada de senhas  
✅ Design moderno usando Bootstrap

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13+
- Django 5.x
- PostgreSQL
- Bootstrap 5
- Django Messages Framework
- Django EmailMultiAlternatives

---

## 🚀 Como Rodar o Projeto

### **1️⃣ Clonar o Repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### **2️⃣ Criar um Ambiente Virtual**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### **3️⃣ Instalar as Dependências**

```bash
pip install -r requirements.txt
```

### **4️⃣ Configurar as Variáveis de Ambiente**

Crie um arquivo **`.env`** na raiz do projeto e adicione as seguintes variáveis:

```ini
SECRET_KEY=SuaChaveSecretaAqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

POSTGRES_DB_NAME=seu_banco
POSTGRES_USER=seu_usuario
POSTGRES_PASS=sua_senha
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seuemail@gmail.com
EMAIL_HOST_PASSWORD=suasenha
EMAIL_USE_TLS=True
```

### **5️⃣ Executar as Migrações**

```bash
python manage.py migrate
```

### **6️⃣ Criar um Superusuário**

```bash
python manage.py createsuperuser
```

### **7️⃣ Rodar o Servidor**

```bash
python manage.py runserver
```

Acesse o sistema no navegador:

```
http://127.0.0.1:8000/
```

---

---

## 🔑 📩 **Autenticação e Registro**

- O usuário se registra com **nome, e-mail e senha**.
- Um **username é gerado automaticamente** a partir do nome (ex: "João Silva" → `joaosilva`).
- Se o username já existir, um **UUID aleatório** será adicionado (`joaosilva1234`).
- O usuário recebe um **e-mail de boas-vindas** com um link para login.

---

## 📧 **Envio de E-mail de Boas-Vindas**

- O sistema envia um **e-mail automático** quando o usuário se registra.
- O e-mail contém:
  - Nome do usuário
  - Mensagem de boas-vindas
  - Link direto para login

---

## 🔐 **Validação de Senha**

- A senha deve conter:
  - Pelo menos **8 caracteres**
  - Pelo menos **1 letra maiúscula**
  - Pelo menos **1 número**
  - Pelo menos **1 caractere especial**
- Se a senha não atender aos critérios, um erro será exibido.

---

## 📌 **Endpoints**

| Método | Rota                  | Descrição                        |
| ------ | --------------------- | -------------------------------- |
| `GET`  | `/`                   | Página inicial (Login)           |
| `POST` | `/accounts/login/`    | Realiza login                    |
| `GET`  | `/accounts/register/` | Página de registro               |
| `POST` | `/accounts/register/` | Cria um novo usuário             |
| `GET`  | `/menu/`              | Página inicial do usuário logado |
| `POST` | `/accounts/logout/`   | Logout do sistema                |

---

## 🛠 **Possíveis Erros e Soluções**

| Erro                       | Causa                                         | Solução                                                   |
| -------------------------- | --------------------------------------------- | --------------------------------------------------------- |
| `Este campo é obrigatório` | O campo pode estar com nome incorreto no HTML | Verifique se o `name=""` do campo no HTML está correto    |
| `E-mail inexistente`       | O usuário não está cadastrado                 | Certifique-se de que o e-mail foi registrado corretamente |
| `Senha inválida`           | O usuário digitou a senha errada              | Tente redefinir a senha se necessário                     |
| `Erro ao enviar e-mail`    | Configuração SMTP incorreta                   | Verifique as credenciais no `.env`                        |

---

## 📜 **Licença**

Este projeto é de código aberto e pode ser usado e modificado livremente.

---

Agora seu **README.md** está completo, profissional e pronto para ser publicado! 🚀🔥

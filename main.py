# variáveis
usuarios = []
postagens = []
proximo_id_usuario = 1
proximo_id_postagem = 1

# funções
def resetar():
    global proximo_id_usuario
    global proximo_id_postagem
    global usuarios
    global postagens
    usuarios.clear()
    postagens.clear()
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def criar_usuario(nome):
    global proximo_id_usuario
    if nome == '':
        raise Exception("Nome não pode ser vazio")
    usuario = {
        'id': proximo_id_usuario,
        'nome': nome,
        'seguidores': [],
        'seguindo': []
    }  
    usuarios.append(usuario)
    proximo_id_usuario += 1

def criar_postagem(usuario, texto):
    global proximo_id_postagem
    if texto == "":
        raise Exception("Texto da postagem não pode ser vazio")
    
    try:
        encontrar_usuario_por_id(usuario)
        postagem = {
            'id': proximo_id_postagem,
            'usuario': usuario,
            'mensagem': texto,
            'curtidores': [],
            'comentarios': []
        }
        postagens.append(postagem)
        proximo_id_postagem += 1
    except IndexError:
        raise IndexError("Usuário não encontrado")

def seguir_usuario(usuario_seguidor, usuario_a_seguir):
    if usuario_seguidor == usuario_a_seguir:
        raise Exception("Não pode seguir a si mesmo")
    
    try:
        seguir = encontrar_usuario_por_id(usuario_seguidor)
        seguir_usuario = encontrar_usuario_por_id(usuario_a_seguir)
        
        seguir['seguindo'].append(usuario_a_seguir)
        seguir_usuario['seguidores'].append(usuario_seguidor)
    except IndexError:
        raise IndexError("Usuário não encontrado")

def curtir_postagem(usuario, postagem):
    try:
        postagem = encontrar_postagem_por_id(postagem)
        if usuario in postagem['curtidores']:
            raise Exception("Você já curtiu esta postagem")
        postagem['curtidores'].append(usuario)
    except IndexError:
        raise IndexError("Postagem não encontrada")

def comentar_postagem(usuario, postagem, texto):
    if not texto.strip():
        raise ValueError("O comentário não pode ser vazio")
    try:
        postagem = encontrar_postagem_por_id(postagem)
        comentario = {
            'usuario': usuario,
            'texto': texto
        }
        postagem['comentarios'].append(comentario)
    except IndexError:
        raise IndexError("Postagem não encontrada")

def encontrar_usuario_por_id(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return usuario
    raise IndexError("Usuário não encontrado")

def encontrar_postagem_por_id(post_id):
    for postagem in postagens:
        if postagem['id'] == post_id:
            return postagem
    raise IndexError("Postagem não encontrada")

def excluir_conta(usuario_id):
    try:
        usuario = encontrar_usuario_por_id(usuario_id)
        for postagem in postagens:
            if postagem['usuario'] == usuario_id:
                postagens.remove(postagem)

        for outro_usuario in usuarios:
            if usuario_id in outro_usuario['seguindo']:
                outro_usuario['seguindo'].remove(usuario_id)
            if usuario_id in outro_usuario['seguidores']:
                outro_usuario['seguidores'].remove(usuario_id)
        
        usuarios.remove(usuario)
    except IndexError:
        raise IndexError("Usuário não encontrado.")


# menu
def exibir_menu():
    while True:
        print("\n--- Menu ---")
        print("1. Criar Usuário")
        print("2. Criar Postagem")
        print("3. Seguir Usuário")
        print("4. Curtir Postagem")
        print("5. Comentar em Postagem")
        print("6. Excluir Conta")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            criar_usuario(nome)
            print("Usuário criado com sucesso!")
        
        elif opcao == "2":
            user_id = int(input("Digite o ID do autor da postagem: "))
            texto = input("Digite o texto da postagem: ")
            try:
                criar_postagem(user_id, texto)
                print("Postagem criada com sucesso!")
            except IndexError:
                print("Usuário não encontrado.")
        
        elif opcao == "3":
            user_id = int(input("Digite o seu ID: "))
            target_id = int(input("Digite o ID do usuário que deseja seguir: "))
            try:
                seguir_usuario(user_id, target_id)
                print("Usuário seguido com sucesso!")
            except IndexError:
                print("Usuário não encontrado.")
            except Exception as e:
                print(f"Erro: {e}")
        
        elif opcao == "4":
            user_id = int(input("Digite o seu ID: "))
            post_id = int(input("Digite o ID da postagem que deseja curtir: "))
            try:
                curtir_postagem(user_id, post_id)
                print("Postagem curtida com sucesso!")
            except IndexError:
                print("Postagem não encontrada.")
            except Exception as e:
                print(f"Erro: {e}")
        
        elif opcao == "5":
            user_id = int(input("Digite o seu ID: "))
            post_id = int(input("Digite o ID da postagem que deseja comentar: "))
            texto = input("Digite o texto do comentário: ")
            try:
                comentar_postagem(user_id, post_id, texto)
                print("Comentário adicionado com sucesso!")
            except IndexError:
                print("Postagem não encontrada.")
        
        elif opcao == "6":
            user_id = int(input("Digite o ID do usuário que deseja excluir: "))
            try:
                excluir_conta(user_id)
                print("Conta excluída com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
        
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Para testar a interface do menu
# exibir_menu()

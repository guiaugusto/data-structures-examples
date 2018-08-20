#include <stdio.h>
#include <stdlib.h>
#define TAMANHO_SIMPLES 100000
#define TAMANHO_INDEXADO 10

void preenche_tabela(int *tabela_simples, int quantidade, int limite){

  int numero;
  int j;

  for(int i = 0; i < quantidade; i++){
    numero = rand() % limite;
    j = 0;

    do{
      if(numero == tabela_simples[i]){
        numero = rand() % limite;
      }else{
        j++;
      }
    }while(j < i);

    tabela_simples[i] = numero;
  }

}

void ordena_tabela(int *tabela_simples, int tamanho){

  int i = tamanho/2;
  int pai, filho;
  int temp;

  while(true){
    if(i > 0){
      i--;
      t = tabela_simples[i];
    }else{
      tamanho--;
      if(tamanho == 0) return;
      t = a[n];
      a[n] = a[0];
    }

    pai = i;
    filho = i * 2 + 1;

    while(filho < n){
      
    }
  }

}

void heapsort(int a[], int n) {
   int i = n / 2, pai, filho, t;
   while(true) {
      if (i > 0) {
          i--;
          t = a[i];
      } else {
          n--;
          if (n == 0) return;
          t = a[n];
          a[n] = a[0];
      }
      pai = i;
      filho = i * 2 + 1;
      while (filho < n) {
          if ((filho + 1 < n)  &&  (a[filho + 1] > a[filho]))
              filho++;
          if (a[filho] > t) {
             a[pai] = a[filho];
             pai = filho;
             filho = pai * 2 + 1;
          } else {
             break;
          }
      }
      a[pai] = t;
   }
}

int main (){

  int tabela_simples[TAMANHO_SIMPLES];
  int tabela_indexada[TAMANHO_INDEXADO];

  int limite;

  printf("Insira um limite: ");
  scanf("%d", &limite);

  preenche_tabela(tabela_simples, TAMANHO_SIMPLES, limite);

  heapsort(tabela_simples, TAMANHO_SIMPLES);

  for(int i = 0; i < TAMANHO_SIMPLES; i++){
    printf("%d\n", tabela_simples[i]);
  }



  return 0;
}

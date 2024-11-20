const fs = require("fs");

// Função Merge Sort
function mergeSort(array) {
  // Caso base: arrays com 1 ou nenhum elemento já estão ordenados
  if (array.length <= 1) {
    return array;
  }

  // Divide o array ao meio
  const meio = Math.floor(array.length / 2);
  const esquerda = array.slice(0, meio);
  const direita = array.slice(meio);

  // Ordena as metades recursivamente e as mescla
  return merge(mergeSort(esquerda), mergeSort(direita));
}

function merge(esquerda, direita) {
  let resultado = [];
  let i = 0; // Índice para a metade esquerda
  let j = 0; // Índice para a metade direita

  // Mescla os dois arrays ordenados
  while (i < esquerda.length && j < direita.length) {
    if (esquerda[i] < direita[j]) {
      resultado.push(esquerda[i]);
      i++;
    } else {
      resultado.push(direita[j]);
      j++;
    }
  }

  // Adiciona os elementos restantes (se houver) de cada metade
  return resultado.concat(esquerda.slice(i)).concat(direita.slice(j));
}

function lerArquivoParaArray(nomeArquivo) {
  try {
    // Lê o arquivo de forma síncrona
    const dados = fs.readFileSync(nomeArquivo, "utf8");

    // Divide o conteúdo do arquivo em linhas e converte cada linha para número
    const array = dados
      .split("\n") // Divide por cada nova linha
      .map((linha) => parseFloat(linha.trim())) // Converte para número
      .filter((numero) => !isNaN(numero)); // Filtra valores inválidos

    return array;
  } catch (erro) {
    console.error("Erro ao ler o arquivo:", erro);
  }
}

function escreverArrayParaArquivo(array, nomeArquivo) {
  try {
    // Junta os elementos do array com quebras de linha e escreve no arquivo
    const conteudo = array.join("\n");
    fs.writeFileSync(nomeArquivo, conteudo, "utf8");
    console.log(`Arquivo "${nomeArquivo}" criado com sucesso!`);
  } catch (erro) {
    console.error("Erro ao escrever no arquivo:", erro);
  }
}

// Medir o tempo de execução
console.time("Tempo de execução");

// Obter informações sobre a versão do Node.js e do sistema operacional
const os = require("os");
const nodeVersion = process.version;
const sistema = os.platform(); // Ex: 'linux', 'darwin', 'win32'
const arquitetura = os.arch(); // Ex: 'x64' ou 'arm'
const memoriaTotal = os.totalmem(); // Memória total do sistema em bytes
const memoriaLivre = os.freemem(); // Memória livre do sistema em bytes

// Medir o uso de memória do processo antes da execução
const memoriaUsoAntes = process.memoryUsage();
console.log("Uso de memória do processo antes da execução:");
console.log(
  "RSS (Resident Set Size):",
  (memoriaUsoAntes.rss / 1024 ** 2).toFixed(2),
  "MB"
);
console.log(
  "Heap Total:",
  (memoriaUsoAntes.heapTotal / 1024 ** 2).toFixed(2),
  "MB"
);
console.log(
  "Heap Used:",
  (memoriaUsoAntes.heapUsed / 1024 ** 2).toFixed(2),
  "MB"
);
console.log(
  "External:",
  (memoriaUsoAntes.external / 1024 ** 2).toFixed(2),
  "MB"
);

// Função exemplo para medir o tempo de execução
let arr = lerArquivoParaArray("arquivoteste.txt");
let arrayOrd = mergeSort(arr);
escreverArrayParaArquivo(arrayOrd, "Resultados/respostasJSMerge.txt");

// Medir o uso de memória do processo após a execução
const memoriaUsoDepois = process.memoryUsage();
console.log("Uso de memória do processo após a execução:");
console.log(
  "RSS (Resident Set Size):",
  (memoriaUsoDepois.rss / 1024 ** 2).toFixed(2),
  "MB"
);
console.log(
  "Heap Total:",
  (memoriaUsoDepois.heapTotal / 1024 ** 2).toFixed(2),
  "MB"
);
console.log(
  "Heap Used:",
  (memoriaUsoDepois.heapUsed / 1024 ** 2).toFixed(2),
  "MB"
);
console.log(
  "External:",
  (memoriaUsoDepois.external / 1024 ** 2).toFixed(2),
  "MB"
);

// Imprimir as informações sobre o sistema
console.timeEnd("Tempo de execução");
console.log("Versão do Node.js:", nodeVersion);
console.log("Sistema operacional:", sistema);
console.log("Arquitetura do processador:", arquitetura);
console.log(
  "Memória total do sistema:",
  (memoriaTotal / 1024 ** 3).toFixed(2),
  "GB"
);
console.log(
  "Memória livre do sistema:",
  (memoriaLivre / 1024 ** 3).toFixed(2),
  "GB"
);

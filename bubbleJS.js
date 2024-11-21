const fs = require("fs");

// Função Bubble Sort
function bubbleSort(arr) {
  let n = arr.length;

  // Loop externo para percorrer o array
  for (let i = 0; i < n - 1; i++) {
    // Flag para otimizar: se não houve trocas, o array já está ordenado
    let trocou = false;

    // Loop interno para comparar e trocar elementos adjacentes
    for (let j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        // Troca os elementos se estiverem na ordem errada
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;

        // Marca que houve uma troca
        trocou = true;
      }
    }

    // Se não houveram trocas, o array já está ordenado
    if (!trocou) {
      break;
    }
  }

  return arr;
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
  (memoriaUsoAntes.rss / 1024).toFixed(2),
  "KB"
);
console.log("Heap Total:", (memoriaUsoAntes.heapTotal / 1024).toFixed(2), "KB");
console.log("Heap Used:", (memoriaUsoAntes.heapUsed / 1024).toFixed(2), "KB");
console.log("External:", (memoriaUsoAntes.external / 1024).toFixed(2), "KB");

// Função exemplo para medir o tempo de execução
let arr = lerArquivoParaArray("arquivoteste.txt");
let arrayOrd = bubbleSort(arr);
escreverArrayParaArquivo(arrayOrd, "Resultados/respostasJSBubble.txt");

// Medir o uso de memória do processo após a execução
const memoriaUsoDepois = process.memoryUsage();
console.log("Uso de memória do processo após a execução:");
console.log(
  "RSS (Resident Set Size):",
  (memoriaUsoDepois.rss / 1024).toFixed(2),
  "KB"
);
console.log(
  "Heap Total:",
  (memoriaUsoDepois.heapTotal / 1024).toFixed(2),
  "KB"
);
console.log("Heap Used:", (memoriaUsoDepois.heapUsed / 1024).toFixed(2), "KB");
console.log("External:", (memoriaUsoDepois.external / 1024).toFixed(2), "KB");

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

# Procedência do pacote V7

Importado em 22/10/2026, a pedido do responsável pelo repositório, como referência da versão mecânica final.

- Arquivo recebido: `Tunel_Hibrido_V7_COMPLETO-20261008T163150Z-1-001 (1).zip`.
- SHA-256 do ZIP: `10ca2523b597eb13e5e1d8e813688b99cbebd137426cbae02610efcd70adb881`.
- Diretório interno: `Tunel_Hibrido_V7_COMPLETO/`.
- Destino no repositório: `modelos-3d/`, preservando nomes e estrutura do pacote.
- 234 arquivos no ZIP: 101 já existiam com conteúdo idêntico; 133 foram incorporados. Nenhum arquivo existente precisou ser substituído.
- O manifesto descreve 232 arquivos; todos passaram na conferência de tamanho e SHA-256. O manifesto e o LEIA_PRIMEIRO da raiz do pacote não integram suas próprias entradas.

## Documentação editorial

O README da raiz e `documentacao/GUIA_DE_MONTAGEM.md` organizam a navegação e a montagem. Os documentos técnicos originais, PDFs, imagens, geometrias, fontes e relatórios foram preservados sem alteração. As alternativas de asa e ligação são explicitadas separadamente no novo roteiro para evitar duplicidade de fabricação.

Há uma cópia adicional da colmeia no checkout anterior, fora do manifesto; ela foi mantida para preservar o conteúdo existente e não acrescenta uma peça à lista de fabricação.

## Alcance das verificações

A importação conferiu integridade e completude em relação ao ZIP e ao manifesto. Os resultados geométricos em `06_CAD_VALIDACAO/relatorio_verificacao.json` são registros fornecidos pelo pacote; a importação não executou novamente os cálculos CAD ou testes de colisão. O visualizador foi validado anteriormente com Chromium/WebGL no ambiente.

Montagem física, corte, impressão, rigidez, tolerâncias, instalação elétrica, calibração e fluxo continuam sujeitos à validação em bancada. Não há firmware ou circuito elétrico implementado neste pacote.

Para repetir a conferência de integridade, execute `python3 ferramentas/verificar_pacote.py` a partir da raiz do repositório. Se as geometrias forem alteradas intencionalmente no futuro, o manifesto original passa a representar somente a versão de origem, e as diferenças devem ser documentadas.

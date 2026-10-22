# Túnel de vento experimental · V7 híbrido

Projeto de túnel de vento para medição experimental de forças aerodinâmicas, desenvolvido no âmbito da bolsa de monitoria e das atividades do laboratório Maker. A versão mecânica de referência é o **Túnel Híbrido V7**: dutos em MDF, câmara e conexões impressas em 3D e tampa de acrílico.

![Conjunto completo V7](modelos-3d/05_VISUALIZACAO/01_conjunto_completo.png)

## Comece aqui

1. Leia o [guia de montagem por etapas](documentacao/GUIA_DE_MONTAGEM.md).
2. Consulte o [manual técnico ilustrado](modelos-3d/04_DOCUMENTOS/01_GUIA_MONTAGEM.md) ou sua [versão PDF](modelos-3d/04_DOCUMENTOS/01_GUIA_MONTAGEM.pdf).
3. Confira a [lista de fabricação](modelos-3d/04_DOCUMENTOS/02_LISTA_FABRICACAO.md) e a [lista de compras](modelos-3d/04_DOCUMENTOS/03_LISTA_COMPRAS.md).
4. Faça os cupons e a montagem a seco antes de fabricar o lote completo.

## Organização

| Pasta | Conteúdo |
|---|---|
| [documentacao](documentacao/) | Guia de entrada, checklist e procedência do pacote final |
| [modelos-3d/01_IMPRESSAO_3D](modelos-3d/01_IMPRESSAO_3D/) | STL finais, alternativas e testes separados |
| [modelos-3d/02_CORTE_LASER](modelos-3d/02_CORTE_LASER/) | Chapas e peças SVG/DXF por material e espessura |
| [modelos-3d/03_COMPRADOS_NAO_FABRICAR](modelos-3d/03_COMPRADOS_NAO_FABRICAR/) | Componentes comerciais e referências de posicionamento |
| [modelos-3d/04_DOCUMENTOS](modelos-3d/04_DOCUMENTOS/) | Manual original, listas, PDFs e resumo de verificação |
| [modelos-3d/05_VISUALIZACAO](modelos-3d/05_VISUALIZACAO/) | Imagens, visualizador HTML e conjunto OBJ/STL |
| [modelos-3d/06_CAD_VALIDACAO](modelos-3d/06_CAD_VALIDACAO/) | Fontes CAD, scripts e relatórios digitais |
| [hardware](hardware/) | Área reservada aos circuitos e componentes reais; ainda sem esquema elétrico |
| [firmware](firmware/) | Área reservada à programação; ainda sem firmware implementado |
| [dados](dados/) | Área reservada aos resultados experimentais |

## Referências da versão final

- Corpo: entrada MDF de 200 mm + câmara de 200 mm + saída MDF de 200 mm.
- Passagem nominal: 120 × 120 mm; painel de referência: 750 × 220 mm.
- Materiais: MDF 3 mm nos dutos, MDF 6 mm nos apoios/base opcional e acrílico 3 mm na tampa.
- Impressão padrão: **19 STL / 29 peças físicas**; seis apoios usam **24 lâminas** de MDF.
- Use a moldura **04_moldura_V7_passagem_120mm.stl**. A moldura histórica em `referencias/` serve somente à regeneração CAD.
- Asa B substitui asa A; ligações 125,8/126,0 substituem a ligação 126,2 conforme o teste de encaixe. Não some alternativas ao lote padrão.

## Visualizar e conferir

Baixe o repositório e abra `modelos-3d/05_VISUALIZACAO/ABRIR_VISUALIZADOR_3D.html` em um navegador com WebGL. O visualizador é independente de internet e permite girar, ocultar materiais e explodir o conjunto. A página de arquivo do GitHub não executa esse HTML.

Para conferir o pacote, execute na raiz: `python3 ferramentas/verificar_pacote.py`. O comando verifica tamanho e SHA-256 dos 232 arquivos descritos no manifesto, sem modificar o projeto. A [procedência](documentacao/PROCEDENCIA_V7.md) registra o arquivo recebido e o resultado da importação.

## Estado do projeto

O pacote inclui relatórios de verificação digital; esses resultados são registros do autor do pacote. A integridade dos arquivos foi conferida na importação. A montagem física, os encaixes reais, a rigidez, a vedação, a calibração e o fluxo ainda precisam de ensaios. O conjunto mede uma componente de força; não separa sustentação e arrasto simultaneamente.

Fonte, controlador, eletrônica de medição e firmware dependem dos componentes reais e não são dimensionados pelo pacote mecânico. Consulte os [limites da verificação](modelos-3d/04_DOCUMENTOS/04_VERIFICACAO_MODELO.md) antes de operar.

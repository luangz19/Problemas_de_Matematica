# 🧮 Repositório de Problemas de Matemática

Programas em Python para resolver exercícios do Ensino Médio (1º, 2º e 3º anos).

## 📚 Tópicos Abordados
- **1º Ano**: Funções, Progressões, Estatística
- **2º Ano**: Matrizes, Análise Combinatória
- **3º Ano**: Cálculo, Probabilidade

## 🛠 Como Usar
```bash
git clone https://github.com/luangz19/Problemas_de_Matemática.git
cd problemas-matematica
pip install -r requirements.txt  # Instala dependências
```

## ✨ Exemplo de Código
```python
from sympy import symbols, solve

x = symbols('x')
solucao = solve(x**2 - 5*x + 6, x)
print("Raízes:", solucao)  # Output: [2, 3]
```

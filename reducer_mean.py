import sys


c_j = 0
m_j = 0


for line in sys.stdin:
    c_k, m_k = map(float, line.strip().split())
    
    c_i = c_j + c_k
    m_i = (c_j * m_j + c_k * m_k)/(c_j + c_k)
    c_j, m_j = c_i, m_i         
            
print(m_j)

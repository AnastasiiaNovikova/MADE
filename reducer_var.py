import sys


c_j = 0
m_j = 0
v_j = 0


for line in sys.stdin:
    c_k, m_k, v_k = map(float, line.strip().split())
    
    c_i = c_j + c_k
    m_i = (c_j * m_j + c_k * m_k)/(c_j + c_k)
    v_i = (
        (c_j * v_j + c_k * v_k)/(c_j + c_k) +
         c_j * c_k * ((m_j - m_k)/(c_j + c_k))**2
        )
    c_j, m_j, v_j = c_i, m_i, v_i           
            
print(m_j, v_j)

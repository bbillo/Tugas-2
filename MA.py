M, N, T = map(int,input().split())

#TRAFFIC LIGHT TIME
red = int(20)
yellow = int(5)
green = int(60)

traffic = T//85
w_jalan = (traffic * green)
m_lewat = w_jalan % ((M+N)*5)


if m_lewat > 0:
    print(f"NO, {m_lewat}")
else:
    print(f"YES, {m_lewat}")
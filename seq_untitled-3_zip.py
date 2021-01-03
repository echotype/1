def Read_Two_Column_File(f):
    with open(f, 'r') as data:
        x = []
        y = []
        for eachline in data:
            p = eachline.split()
            
            x.append(p[0])
            y.append(p[1])
            
                
                
            
    return x, y
def main():
    
    x, y = Read_Two_Column_File('/Users/pat/documents/_____2_(project)/enzymes_emboss_e.011.txt')
    
    dictionary = dict(zip(x, y))
    print(dictionary)

    
    
main()

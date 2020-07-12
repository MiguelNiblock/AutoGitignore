class AutoGitignore:
    
    def __init__(self):
        import os
        self.res = ''

    def search(self,
               marker, # a file to find. for example: 'include.txt'
               path
              ): 
        import os
        res = ''
        passlst = []
        hasmarker = False
        
        # Is there a marker in this path?
        for i in os.listdir(path):
            
            if i == '.git':
                continue
            
            if os.path.isdir(path+'/'+i):
                newpath = path+'/'+i
                newres,newpasslst = self.search(marker=marker, path = newpath)
                res = res+newres
                passlst = passlst+newpasslst
            
            elif i == marker:
                hasmarker = True
                passlst.append(path[1:]+'/')
        #####################################    
        if not hasmarker:

            for i in os.listdir(path):
                if not os.path.isdir(path+'/'+i):
                    res = res+path[1:]+'/'+i+'\n'

        return res,passlst
    
    def subfolders(self,
                   res,
                   passlst,
                  ):
        res = res.split('\n')
        newres = []
        for i in res:
            issub = False
            for keeper in passlst:
                if keeper == i[:len(keeper)]:
                    issub = True
                    
            if not issub:
                newres.append(i)
        return '\n'.join(newres)
    
    def run(self,
            marker='include.txt',
            path='.'
           ):
        import os
        print('Searching for markers in folders...')
        self.res,self.passlst = self.search(marker,path)
        self.res = marker+'\n'+self.res
        print('Keeping files inside subfolders...')
        self.res = self.subfolders(res=self.res,passlst=self.passlst)
        print('\nFiles to Ignore:\n')
        print(self.res)
        
    def save(self,
             filename='py.gitignore'):
        print('saving',filename)
        file = open(filename,'w') 
        file.write(self.res)
        file.close()
        print('done')

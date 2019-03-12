data = myfiles.readlines(1000)
    for bytecode in data:
        print(bytecode.rsplit('\n',''))   
        for words in data:
            pattern = '%{WORD} @ %{GREEDYDATA} %{WORD} %{WORD:bytecodes}'
            grok = Grok(pattern)
            print (grok.match(data))

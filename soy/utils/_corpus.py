class DoublespaceLineCorpus:
    
    def __init__(self, corpus_fname, num_doc = -1, num_sent = -1, iter_sent = False):
        self.corpus_fname = corpus_fname
        self.num_doc = num_doc
        self.num_sent = num_sent
        self.iter_sent = iter_sent

        is_part = False
        num_sent_tmp = 0
        
        with open(corpus_fname, encoding='utf-8') as f:
        
            for doc_id, doc in enumerate(f):

                if (num_doc > 0) and (doc_id + 1 == num_doc):
                    is_part = True
                    break

                for sent in doc.split('  '):
                    if not sent.strip():
                        continue
                    num_sent_tmp += 1

                    if (num_sent > 0) and (num_sent_tmp == num_sent):
                        is_part = True
                        break
                
            self.num_doc = doc_id + 1
            self.num_sent = num_sent_tmp
        
        print('DoublespaceLineCorpus %s has %d docs, %d sents' % ('(partial)' if is_part else '', self.num_doc, self.num_sent))
                

    def __iter__(self):
        
        with open(self.corpus_fname, encoding='utf-8') as f:
            
            for doc_id, doc in enumerate(f):
                
                if doc_id >= self.num_doc:
                    break
                    
                if not self.iter_sent:
                    yield doc
                    
                else:
                    for sent in doc.split('  '):
                        sent = sent.strip()
                        if not sent:
                            continue
                        yield sent.strip()
    
    
    def __len__(self):
        return self.num_sent if self.iter_sent else self.num_doc
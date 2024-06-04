class Solution:
    def groupAnagrams(self, strs):
        # 1
        # for each word
            # make an array to count characters
            # make a string from the counts array
            # use encoding string as key and array as value in word hash
            # append word to word hash array
        # return all values in word hash

        words = {}
        for word in strs:
            char_counts = [ 0 ] * 26
            for char in word:
                idx = ord(char) - ord('a')
                char_counts[idx] += 1
            
            # have to use a delimiter to avoid confusion with 1,0 and 10
            encoding = ','.join([str(count) for count in char_counts])
            
            if encoding in words:
                words[encoding].append(word)
            else:
                words[encoding] = [word]
        
        return words.values()
# venuesearch

### usage:
1. The references must be copied to a text file (Suggestion, open using word, then copy to vim/gedit/notepad to remove any formatting)
2. The generated output is sorted according to name to reveal common venues (the file type is .csv so that any resideual soritng can be done Excel etc..)


### output:
1. csv file (default name: `output.csv`) which contains the extracted journal/venue names
2. Output message showing what percentage of references were captured successfully.
```python
 . 
 . 
 . 
 ICTIS, IEEE, pp. 503–510.',
 'IEEE Commun  Surv  Tutor  21 (3), 2224–2287',
 '2018 10th International Conference on Intelligent Human-Machine Systems and '
 'Cybernetics. Vol. 2. IHMSC, IEEE, pp. 164–169.',
 '2019 Chinese Automation Congress. CAC, IEEE, pp. 782–787.']


 94.7 % references captured successfully
 
Process finished with exit code 0
```



### Considerations 
1. Reading from pdf is not implemented yet 
2. ArXiV's will just show up at AxXiV; No google search is done


### Improvements
1. If the references has italics for the venue: (Bingo, we can use that :) 
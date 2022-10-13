## Symmetric Encryption using Artificial Neural Network, Binary Tree Traversal, and Interleaving Salting

* This repository contains the code of a novel way of symmetric encryption utilizing interleaving salting, Binary Tree traversal, and an Artificial Neural Network in a sequential manner. 

* Knowledge of the encryption pipeline, salt, and neural network weights is required for decryption. As the same set of values is required for encryption and decryption, our proposed approach is a type of symmetric-key algorithm. 

* Each user will have a unique key. Thus if a key attributing to a particular user is compromised, the integrity of the data of the remaining users will still be maintained. 

* Our approach can be utilized to encrypt text data such as messages, documents, and letters. 

**Our approach has been puplished as a research paper in the International Journal of Engineering and Advanced Technology (IJEAT). Link to the paper: [IJEATPaperLink](https://www.ijeat.org/portfolio-item/f37220811622/)** 

### Usage and Options
Usage
```
python main.py 
```
Options
```
  -input --input_data         String to be encrypted and decrypted [default: "Hey! I love Machine Learning"]
  -s --salt                   salt used for encryption [default: "123456789"]
  -u --user_id                User Id of the user, unique for each user [default: 1]
```

### Sample Input and Output
Sample Input(user 1 encrypting and decrypting a simple message):
```
python main.py --input_data "Hey this is a sample message to be encrypted" --salt "1357986420" --user_id 1
```
Output of the sample input:
```
The encrypted value is:
 [[[ 3.37583812e+05  1.64542906e+05  2.45194500e+05  1.01181008e+05
    2.06988281e+05  7.87371016e+04  7.47727891e+04  2.96236312e+05
    4.18198500e+05  1.65167547e+05  2.35464750e+05 -2.01571875e+03
    8.23929141e+04  2.50490125e+05  2.59946094e+05  1.07921055e+05]]

 [[ 1.49142594e+05  8.74580000e+04  1.34142562e+05  4.89858203e+04
    8.63449375e+04  5.38032578e+04  4.46780898e+04  1.29969156e+05
    2.04914969e+05  7.90371406e+04  1.38504266e+05  5.43599609e+03
    4.31102344e+04  1.26556719e+05  1.50327719e+05  4.42520117e+04]]

 [[ 3.29476312e+05  1.78499531e+05  2.91490875e+05  1.09278055e+05
    1.95814562e+05  8.48656328e+04  3.69958398e+04  2.72682812e+05
    4.36975875e+05  1.76299344e+05  2.53977453e+05  5.40903125e+03
    8.89624453e+04  2.97742000e+05  3.29796125e+05  9.15846016e+04]]

 [[ 2.00799484e+05  8.66614062e+04  1.18761453e+05  6.09935039e+04
    1.55794688e+05  7.64994297e+04  8.88769609e+04  2.26754562e+05
    3.18205375e+05  1.25407734e+05  1.17167766e+05 -6.19490039e+03
    6.75352266e+04  1.53901141e+05  1.77494734e+05  1.00697266e+05]]

 [[ 1.35299297e+05  6.86652188e+04  7.92241641e+04  4.61883672e+04
    1.11692516e+05  6.70251562e+04  1.08589055e+05  1.61886266e+05
    2.37075078e+05  8.72115625e+04  1.33261828e+05  2.32083398e+03
    5.05025156e+04  1.27996781e+05  1.57766422e+05  7.50674531e+04]]

 [[ 7.75652500e+04  3.90160703e+04  4.60552344e+04  3.37941172e+04
    6.36035547e+04  4.73487891e+04  1.05517875e+05  9.11316641e+04
    1.45090625e+05  5.99257188e+04  6.68673047e+04  3.43274707e+03
    1.49322412e+04  6.86950625e+04  9.58348438e+04  6.33371680e+04]]

 [[ 2.45358094e+05  1.06665398e+05  1.52232781e+05  5.68998438e+04
    1.40318578e+05  7.29744688e+04  7.36188672e+04  2.37223594e+05
    3.15708250e+05  1.22729484e+05  2.09911375e+05  1.37099531e+04
    7.85496094e+04  1.80126078e+05  1.97892578e+05  4.57128359e+04]]

 [[ 1.67627516e+05  8.83080938e+04  1.48452719e+05  5.81833750e+04
    1.03642391e+05  7.50969531e+04  4.97541016e+04  1.56664656e+05
    2.45638672e+05  9.68282031e+04  1.42864156e+05 -3.34492188e+02
    5.07904375e+04  1.33560953e+05  1.62851859e+05  6.13351641e+04]]

 [[ 1.90669594e+05  1.04059508e+05  1.90453188e+05  6.10918438e+04
    7.95318750e+04  8.77237188e+04  7.57049531e+04  1.89704094e+05
    3.12718312e+05  1.12534703e+05  2.41173438e+05  1.96475762e+04
    8.91785078e+04  2.13441906e+05  2.82089344e+05  1.14500000e+04]]

 [[ 2.34769094e+05  1.15098922e+05  1.89072312e+05  6.30570391e+04
    1.05273750e+05  7.21481953e+04  8.20416562e+04  1.83133156e+05
    2.76345625e+05  1.12727281e+05  2.10171719e+05  2.68091504e+04
    6.31713047e+04  1.66909688e+05  2.09092297e+05  3.66199844e+04]]

 [[ 1.96806859e+05  1.08218828e+05  1.59347594e+05  4.37918867e+04
    7.98854219e+04  1.01912656e+05  1.13058125e+05  1.55100812e+05
    2.62142953e+05  1.07839484e+05  2.43823750e+05  3.56347734e+04
    6.41248125e+04  1.51439406e+05  2.00855703e+05  1.18694141e+04]]

 [[ 1.25709922e+05  5.99028047e+04  6.42301094e+04  4.27715625e+04
    1.00238867e+05  5.03077891e+04  1.09027344e+05  1.33417406e+05
    1.92668609e+05  7.83793984e+04  7.69178516e+04  8.00875000e+02
    2.45018477e+04  8.88837734e+04  1.06652984e+05  8.06047656e+04]]]
The decrypted value is: Hey this is a sample message to be encrypted
SUCCESS!!
```

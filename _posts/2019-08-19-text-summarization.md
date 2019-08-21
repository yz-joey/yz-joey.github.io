---
layout: post
title: "[Paper] Text Summarization"
description: "Text Summarization"
comments: true
---

### [INLG 2018] [Generation of Company descriptions using concept-to-text and text-to-text deep models: dataset collection and systems evaluation](https://www.aclweb.org/anthology/W18-6532)

* study the performance of several state-of-the-art sequence-tosequence models applied to generation of short company descriptions
* a newly created and publicly available company dataset that has been collected from Wikipedia, which consists of around **51K company descriptions** [(Download)](https://gricad-gitlab.univ-grenoble-alpes.fr/getalp/wikipediacompanycorpus) that can be used for both concept-to-text and text-to-text generation tasks
* the dataset is **not ideal for machine learning** since the abstract, the body and the infobox are only **loosely correlated**

---------------------------------------
<img src="{{site.url}}/images/tgfif/wiki.png" alt="drawing" width="400"/>

---------------------------------------
* the basic model used for generating company description is based on the [**RNN seq2seq model architecture** (Sutskever et al., 2014)](https://github.com/google/seq2seq/) which is divided into two main blocks: **encoder** which encodes the input sentence into fixed-length vector, and the **decoder** that decodes the vector into sequence of words
* as pointed out by (See et al., 2017) the classical seq2seq models suffer from two commonly known problems: repetition of subsequences and wording off-topic 
* repetition is caused at the decoding stage, when the **decoder relies too much on the previous output leading to infinite cycle**; to deal with this problem is to use a coverage mechanism (Tu et al., 2016): used in machine translation, uses the **attention weights to penalize the decoder** for attending to input that has already been attended to previously 
* hallucination can appear when the **word to predict is infrequent** in the training set and therefore has a poor word embedding making it close to a lot of other words; [**Pointer-Generator Network (See et al., 2017)** ](https://github.com/abisee/pointer-generator) which computes a generation probability p_gen ∈ [0, 1]. This value evaluates the probability of 'generating' a word based on the vocabulary known by the model, versus copying a word from the source
* standard automatic measures BLEU (Papineni et al., 2002), ROUGE-L (Lin and Hovy, 2003), Meteor (Denkowski and Lavie, 2014) and CIDEr (Vedantam et al., 2015) were computed using the E2E challenge script.


### [ACL2019] [Multi-Style Generative Reading Comprehension](https://arxiv.org/pdf/1901.02262.pdf)

* reading comprehension (RC) is a challenge task to answer a question given textual evidence provided in a document set
* generative models suffer from **a dearth of training data** to cover open-domain questions
* tackles **generative reading comprehension** (RC), which consists of **answering questions** based on textual evidence and **natural language generation** (NLG)
	* focuses on generating a summary from the question and multiple passages instead of extracting an answer span from the provided passages -->  introduce the [pointer-generator mechanism](https://arxiv.org/pdf/1704.04368.pdf) (See et al., 2017) for generating an abstractive answer from the question and multiple passages by extending to a **Transformer** one that allows words to be **generated from a vocabulary** and to be **copied from the question and passages**
	* learns **multi-style answers** within a model to improve the NLG capability for all styles involved --> also extend the pointer-generator to **a conditional decoder** by introducing an artificial token corresponding to each style

<img src="{{site.url}}/images/tgfif/masque.png" alt="masque" width="450"/>
<img src="{{site.url}}/images/tgfif/multisource.png" alt="multisource" width="400"/>


### [NAACL2019] [Keyphrase Generation: A Text Summarization Struggle](https://www.aclweb.org/anthology/N19-1070)

* Problems of most existing keyphrase generation methods:
	* First, they are not able to find **an optimal value for N** (number of keywords to generate for an article) based on article contents and require it as a preset parameter. 
	* Second, the **semantic and syntactic properties** of article phrases (considered as candidate keywords) are **analyzed separately**. The meaning of longer text units like paragraphs or entire abstract/paper is missed. 
	* Third, **only phrases that do appear in the paper are returned**. In practice, authors do often assign words that are not part of their article. 
* Meng et al. (2017) overcome the second and third problem using an **encoder-decoder model (COPYRNN)** with a bidirectional Gated Recurrent Unit (GRU) and a forward GRU with attention.
* we explore **abstractive text summarization models** proposed in the literature, trained with article abstracts and titles as sources and keyword strings as targets. 
* [**Pointer-Generator network (POINTCOV)**](https://arxiv.org/pdf/1704.04368.pdf) is composed of an **attention-based encoder** that produces the context vector. The decoder is extended with a **pointer-generator model** that computes a probability p_gen from the context vector, the decoder states, and the decoder output.

<img src="{{site.url}}/images/tgfif/scores.png" alt="scores" width="650"/>

* The results show that the tried text summarization models perform poorly on full-match keyword predictions. Their higher ROUGE scores further indicate that the problem is not entirely in the summarization process.

### [ACL 2017] [Deep Keyphrase Generation](https://aclweb.org/anthology/P17-1054) [[code]](https://github.com/memray/seq2seq-keyphrase)

* propose a generative model for keyphrase prediction with an encoder-decoder framework
	* could identify keyphrases that do not appear in the text
	* capture the real semantic meaning behind the text 
* To apply the RNN Encoder-Decoder model, the data need to be converted into **text-keyphrase pairs** that contain only **one source sequence and one target sequence**
*  the RNN is **not able to recall** any keyphrase that contains out-ofvocabulary words --> [copying mechanism (Gu et al., 2016)](https://www.aclweb.org/anthology/P16-1154) is one feasible solution that enables RNN to predict **out-of-vocabulary words** by **selecting appropriate words** from the source text
![copyrnn model]({{site.url}}/images/tgfif/copyrnn.png)

---------------------------------------

### [ACL 2017] [Get To The Point: Summarization with Pointer-Generator Networks](https://arxiv.org/pdf/1704.04368.pdf) [[Tensorflow Python2]](https://github.com/abisee/pointer-generator) [[Tensorflow Python3]](https://github.com/becxer/pointer-generator/) [[Pytorch Python2]](https://github.com/atulkum/pointer_summarizer) [[Data Prepossessing]](https://github.com/abisee/cnn-dailymail)

* Neural **sequence-to-sequence models** have provided a viable new approach for abstractive text summarization but have two shortcomings: 
	* they are liable to reproduce **factual details inaccurately**
	* they tend to **repeat** themselves
* augments the standard sequence-to-sequence attentional model in two orthogonal ways
	* copy words from the source text via pointing 
	* use coverage to keep track of what has been summarized
* Although our best model is abstractive, it **does not produce novel n-grams** (i.e., n-grams that don’t appear in the source text) as often as the reference summaries. The baseline model produces more novel n-grams, but many of these are erroneous
![summarization model]({{site.url}}/images/tgfif/pointer.png)

---------------------------------------

### [SIGIR 2019] [DivGraphPointer: A Graph Pointer Network for Extracting Diverse Keyphrases](https://edward-sun.github.io/files/DivGraphPointer.pdf)

* presents an end-to-end method called DivGraphPointer for extracting a set of diversified keyphrases from a document
* given a document, a word graph is constructed from the document based on **word proximity** and is encoded with **graph convolutional networks**
*  effectively capture document-level word salience by modeling **long-range dependency** between words in the document and **aggregating multiple appearances of identical words** into one node
*  propose a diversified point network to generate a set of diverse keyphrases **out of the word graph** in the decoding process

![graphpointer model]({{site.url}}/images/tgfif/graphpointermodel.png)
![graphpointer results]({{site.url}}/images/tgfif/graphpointer.png)

---------------------------------------

### [arxiv19] [The Curious Case of Neural Text Degeneration](https://arxiv.org/pdf/1904.09751.pdf)

<img src="{{site.url}}/images/tgfif/beamsearch.png" alt="scores" width="350"/>
<img src="{{site.url}}/images/tgfif/beamsearch2.png" alt="scores" width="350"/>

### [arxiv19] [SenseBERT: Driving Some Sense into BERT](https://arxiv.org/pdf/1908.05646.pdf)
* propose a method to employ selfsupervision directly at the word sense level
* SenseBERT is pre-trained to predict not only the masked words but also their WordNet supersenses -->  a lexical-semantic level language model

![sensebert]({{site.url}}/images/tgfif/sensebert.png)
# Progetto WebMining

Il file distance_minhash.py transforma i testi di tutte le canzoni in vettori hash con shingles di una parola, calcola per ogni vettore generato la distanza con i vettori di ogni altra canzone e salva il risultato nel json minhash_dist.json. 
Lo script di cui sopra, prende come input la lista di tutte le canzoni (che non mandiamo per motivi di spazio), ne estrae gli hash e li confronta a due a due (evitando di ripeterne i confronti di testi gia' fatti). Oltre a salvare il dizionario generato, stampa i migliori suggerimenti delle canzoni, e confronta la stima di Jaccard effettuata con minHash, con l'attuale valore di Jaccard. Tale approssimazione è molto vicina al valore reale. Alleghiamo parte dell'output generato (distances_minhash.out).

```
$ python3 distances_minhash.py
Shingling songs...

Shingling 4519 docs took 477.60 sec.

Average shingles per doc: 897.46

Generating random hash functions...

Generating MinHash signatures for all documents...

Generating MinHash signatures took 16.23sec

Comparing all signatures...

Comparing MinHash signatures took 445.66sec

List of Document Pairs with J(d1,d2) more than 0.5
Values shown are the estimated Jaccard similarity and the actual
Jaccard similarity.

		                                                                            Est. J	Act. J
Cristiano_De_André#Tutti_quanti_hanno_bisogno --> Cristina_Donà#Nel_Mio_Giardino	0.59	0.54
Cristiano_De_André#Tutti_quanti_hanno_bisogno --> Daniele_Groff#Every_Day	0.59	0.52
Cristiano_De_André#Tutti_quanti_hanno_bisogno --> Daniele_Groff#Vivere_Per_Sempre	0.57	0.58
Cristiano_De_André#Tutti_quanti_hanno_bisogno --> Daniele_Silvestri#A_Me_Ricordi_Il_Mare	0.66	0.60
Cristiano_De_André#Tutti_quanti_hanno_bisogno --> Daniele_Silvestri#Amarsi_Cantando	0.58	0.56
Cristina_Donà#Nel_Mio_Giardino --> Daniele_Groff#Every_Day	0.79	0.70
Cristina_Donà#Nel_Mio_Giardino --> Daniele_Groff#Vivere_Per_Sempre	0.73	0.70
Cristina_Donà#Nel_Mio_Giardino --> Daniele_Silvestri#A_Me_Ricordi_Il_Mare	0.74	0.64
Cristina_Donà#Nel_Mio_Giardino --> Daniele_Silvestri#Amarsi_Cantando	0.67	0.64
Cristina_Donà#Nel_Mio_Giardino --> Daniele_Silvestri#Dove_sei	0.79	0.67
Daniele_Groff#Every_Day --> Daniele_Groff#Vivere_Per_Sempre	0.72	0.67
Daniele_Groff#Every_Day --> Daniele_Silvestri#A_Me_Ricordi_Il_Mare	0.81	0.77
Daniele_Groff#Every_Day --> Daniele_Silvestri#Amarsi_Cantando	0.77	0.70
Daniele_Groff#Every_Day --> Daniele_Silvestri#Dove_sei	0.86	0.76
Daniele_Groff#Every_Day --> Daniele_Silvestri#Gino_E_L'Alfetta	0.77	0.73
Daniele_Groff#Vivere_Per_Sempre --> Daniele_Silvestri#A_Me_Ricordi_Il_Mare	0.75	0.67
Daniele_Groff#Vivere_Per_Sempre --> Daniele_Silvestri#Amarsi_Cantando	0.59	0.58
Daniele_Groff#Vivere_Per_Sempre --> Daniele_Silvestri#Dove_sei	0.72	0.63
Daniele_Groff#Vivere_Per_Sempre --> Daniele_Silvestri#Gino_E_L'Alfetta	0.78	0.73
Daniele_Groff#Vivere_Per_Sempre --> Daniele_Silvestri#Idiota	0.72	0.65
Daniele_Silvestri#A_Me_Ricordi_Il_Mare --> Daniele_Silvestri#Amarsi_Cantando	0.77	0.74
Daniele_Silvestri#A_Me_Ricordi_Il_Mare --> Daniele_Silvestri#Dove_sei	0.83	0.74
Daniele_Silvestri#A_Me_Ricordi_Il_Mare --> Daniele_Silvestri#Gino_E_L'Alfetta	0.84	0.77
Daniele_Silvestri#A_Me_Ricordi_Il_Mare --> Daniele_Silvestri#Idiota	0.88	0.80
Marta_sui_tubi#Lauto_Ritratto --> Massimo_Ranieri#Se_bruciasse_la_città	0.62	0.53
Marta_sui_tubi#Lauto_Ritratto --> Mau_Mau#An_Viagi	0.63	0.60
Marta_sui_tubi#Lauto_Ritratto --> Giorgia#E_Poi/R	0.66	0.62
Marta_sui_tubi#Lauto_Ritratto --> Giorgia#Father	0.62	0.61
Marta_sui_tubi#Lauto_Ritratto --> Giorgia#In_vacanza_con_me	0.59	0.59
Massimo_Ranieri#Se_bruciasse_la_città --> Mau_Mau#An_Viagi	0.78	0.70
Massimo_Ranieri#Se_bruciasse_la_città --> Giorgia#E_Poi/R	0.75	0.69
Massimo_Ranieri#Se_bruciasse_la_città --> Giorgia#Father	0.74	0.67

```

Il json generato (che si trova nello zip allegato) verra' utilizzato dallo script recommendation.py .  Il sistema di raccomandazioni chiede di inserire il titolo di una canzone. L'utente puo' inserire il titolo completo di una canzone o parte di essa oppure puo' inserire il nome di un'artista o parte di esso. 
Il sistema provera' a indovinare qual è la canzone che l'utente chiede e ne chiedera' conferma. 
Dopodicchè restituira' le 5 migliori raccomandazioni, sulla base della distanza calcolata. 
Per uscire dal programma basta inserire come input il carattere x
Se non vengono in mente canzoni da passare come input, è possibile inserire come input il carattere h o la stringa help, così facendo il sistema prendera' 5 canzoni random dal dataset e le stampera' a video. 
In allegato mettiamo pure un esempio di output dall'esecuzione.
Lo script è eseguibile con `python recommendation.py`

```
> $ python3 recommendation.py
#############
Welcome! This is the system that take as input a song and it will suggest a list of {} songs similar to it calculated with a estimated Jaccard Similarity (MinHash)
These are example songs which you can choose from
	Wilson Pickett - Un'avventura
	Moltheni - Nutriente
	Paola e Chiara - A modo mio
	Sally Oldfield - I sing for you
	I Gens - La stagione di un fiore
	Bruno Rosettani & Trio Aurora - Zucchero e pepe
	Mau Mau - An Viagi
	Marina Rei - Pazza Di Te
	Mario Castelnuovo - Nina
	Ivano Fossati - Lindbergh
Write 'x' to stop the program
If you want help, you might write 'h' or 'help' to show a list of songs you might look for
#############
Please enter the author or the title of a song (or part of it): a modo mio
Maybe you meant A Modo Mio by Negrita? [Y/n]
n
Maybe you meant A modo mio by Paola e Chiara? [Y/n]
n
Maybe you meant A modo mio by Gianni Nazzaro? [Y/n]
n
Sorry, I didn't quite catch the song you're referring too, please try again
Please enter the author or the title of a song (or part of it): a modo mio
Maybe you meant A Modo Mio by Negrita? [Y/n]

Good choice
You chose A Modo Mio by Negrita


Here the list of suggested songs:
 La pianta tè by Ivano Fossati 	0.921875
 Straordinariamente by Adriano Celentano 	0.8671875
 Cerco un gesto naturale by Giorgio Gaber 	0.8671875
 Se le cose stanno così by Sergio Endrigo 	0.859375
 Karma Parente by Marco Parente 	0.859375

Please enter the author or the title of a song (or part of it): La pianta te
Maybe you meant La pianta tè by Ivano Fossati? [Y/n]
yes
Good choice
You chose La pianta tè by Ivano Fossati


Here the list of suggested songs:
 A Modo Mio by Negrita 	0.921875
 Il mare immenso by Giusy Ferreri 	0.90625
 Offeso by Niccolò Fabi 	0.890625
 Per Le Mie Mani by Luca Dirisio 	0.8828125
 L'Uomo Che Amava Le Donne by Nina Zilli 	0.8828125

Please enter the author or the title of a song (or part of it): h
These are example songs which you can choose from
	Natalino Otto - Mogliettina
	Leila Selli - Sola in due
	Ligabue - Balliamo sul mondo
	Giorgio Gaber - Mai, mai, mai, Valentina
	Aurelio Fierro - Lì per lì
	Ricchi e Poveri - Dolce frutto
	Sergio Endrigo - Ci Vuole Un Fiore
	Laura Pausini - La solitudine
	Negrita - Paradisi Per Illusi
	Rossana Casale & Grazia Di Michele - Gli amori diversi
Please enter the author or the title of a song (or part of it): Gli Amori
Maybe you meant Gli amori by Toto Cutugno? [Y/n]
n
Maybe you meant Gli amori diversi by Rossana Casale & Grazia Di Michele? [Y/n]
y
Good choice
You chose Gli amori diversi by Rossana Casale & Grazia Di Michele


Here the list of suggested songs:
 Lì per lì by Aurelio Fierro 	0.9453125
 Re di cuori by Caterina Caselli 	0.9375
 Nina by Mario Castelnuovo 	0.9375
 Re di cuori by Nino Ferrer 	0.9375
 Un piccolo amore by Alina 	0.9296875

Please enter the author or the title of a song (or part of it): Nina
Maybe you meant L'Inferno by Nina Zilli? [Y/n]
y
Good choice
You chose L'Inferno by Nina Zilli


Here the list of suggested songs:
 Abbiamo vinto un'altra guerra by Motta 	0.890625
 No amore by Sacha Distel 	0.875
 Frisco by Paolo Conte 	0.875
 No amore by Giusy Romeo 	0.875
 Maledetta primavera by Loretta Goggi 	0.875

Please enter the author or the title of a song (or part of it): x
Thank you!

``` 

N.B.: Gli script sono stati sviluppati e testati con Python3.6

Il JSON per semplicita' contiene, per ogni canzone, le 20 canzoni con "estimated Jaccard similarity" piu' alto. 
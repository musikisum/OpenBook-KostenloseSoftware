# -*- encoding: UTF-8 -*-

kern=u"""

// user4 = fi correction

if (frsp)
french_punct { kern.x = 87m } / _ { u_frsp == 1 } ;
p("colon") { kern.x = 0m } / _ p("colon");
p("colon") { kern.x = 0m } / p("colon") _;
french_punct { kern.x = 0m } / leftpunct _;
french_punct { kern.x = 0m } / quots _ quots;
french_punct { kern.x = 0m } / p("bracketleft") _;
french_punct { kern.x = 0m } / u(0x00BB) _ u(0x00AB);

// guillemets

letters { kern.x = 100m } / u(0x00AB) _;
u(0x00BB) { kern.x = 125m } / letters _;
quots { kern.x = 100m } / u(0x00AB) _;
u(0x00BB) { kern.x = 125m } / quots _;
u(0x00BB) { kern.x = 125m } / french_punct _;

endif;


// right aligned for 1em length
if (algn == 1)
ANY { kern.x = 2000m - @2.advancewidth } / ZWSP _;
ANY { kern.x = 2000m - @2.advancewidth - @3.advancewidth } / ZWSP _ ANY;
ANY { kern.x = 2000m - @2.advancewidth - @3.advancewidth - @4.advancewidth } / ZWSP _ ANY ANY;
ANY { kern.x = 2000m - @2.advancewidth - @3.advancewidth - @4.advancewidth - @5.advancewidth } / ZWSP _ ANY ANY ANY;

// right aligned for 2-character length
else if (algn == 2)

ANY { kern.x = @2.advancewidth } / ZWSP _;
ANY { kern.x = 0 } / ZWSP _ ANY;
ANY { kern.x = -@2.advancewidth } / ZWSP _ ANY ANY;
ANY { kern.x = -@2.advancewidth * 2} / ZWSP _ ANY ANY ANY;

// right aligned for 3-character length
else if (algn == 3)

ANY { kern.x = 2 * @2.advancewidth } / ZWSP _;
ANY { kern.x = @2.advancewidth } / ZWSP _ ANY;
ANY { kern.x = 0 } / ZWSP _ ANY ANY;
ANY { kern.x = -@2.advancewidth } / ZWSP _ ANY ANY ANY;

else if (algn == 4)

ANY { kern.x = 3 * @2.advancewidth } / ZWSP _;
ANY { kern.x = 2 * @2.advancewidth } / ZWSP _ ANY;
ANY { kern.x = @2.advancewidth } / ZWSP _ ANY ANY;
ANY { kern.x = 0 } / ZWSP _ ANY ANY ANY;


endif;

"""

kern_linlib = u"""

// pnum sups
if (pnum)
p("one.superior") { kern.x = -37m; };
p("two.superior", "four.superior", "five.superior", "six.superior", "seven.superior", "eight.superior") { kern.x = -14m; };
p("three.superior", "nine.superior") { kern.x = -9m; };
p("one.superior", "four.superior") { kern.x = -55m; } / p("one.superior") _; 
p("four.superior") { kern.x = -75m; } / p("seven.superior") _; 
p("six.superior") { kern.x = -55m; } / p("seven.superior") _; 
p("zero.superior", "three.superior", "five.superior", "eight.superior", "nine.superior") { kern.x = -35m; } / p("seven.superior") _; 
ANY { kern.x = -28m; } / p("one.superior") _; 
endif;

// put asterisk above the subscript
u(0x002A) { kern.x = (@1.pos.x - @2.pos.x) ; adv.x = -(@2.pos.x - @1.pos.x) + @1.bb.width + 50m } / cidx3 _ { @2.bb.width <= @1.bb.width };
u(0x002A) { kern.x = (@1.pos.x - @2.pos.x) } / cidx3 _;

// subscript letter
cidx2 { kern.x = (@1.pos.x - @2.pos.x) ; adv.x = -(@2.pos.x - @1.pos.x) + @1.bb.width + 50m } / cidx3 _ { @2.bb.width <= @1.bb.width };
cidx2 { kern.x = (@1.pos.x - @2.pos.x) } / cidx3 _;

cidx3 { kern.x =  @1.pos.x + @1.bb.width - @3.pos.x } / cidx3 cidx2 _;
cidx2 { kern.x =  @2.bb.width - @3.bb.width } / cidx3 cidx2 cidx3 _;
cidx3 { kern.x =  @1.bb.width - @2.bb.width + @3.bb.width - @4.bb.width } / cidx3 cidx2 cidx3 cidx2 _;
cidx2 { kern.x = -@1.bb.width + @2.bb.width - @3.bb.width + @4.bb.width - @5.bb.width } / cidx3 cidx2 cidx3 cidx2 cidx3 _;

// nut fraction
if (frac==2)
cnumsup { kern.x = (@2.advancewidth - @1.advancewidth)/2 } / _ {user1==true} dashes;
cnumsup { kern.x = (@3.advancewidth - @1.advancewidth - @2.advancewidth)/2 } / _ {user1==true} cnumsup dashes;
cnumsup { kern.x = (@4.advancewidth - @1.advancewidth - @2.advancewidth - @3.advancewidth)/2 } / _ {user1==true} cnumsup cnumsup dashes;

dashes { kern.x = -@2.advancewidth + (@2.advancewidth - @1.advancewidth)/2; kern.y = 0m } / cnumsup {user1==true} _ cnumsub;
dashes { kern.x = -@3.advancewidth + (@3.advancewidth - @1.advancewidth - @2.advancewidth)/2; kern.y = 0m } / cnumsup {user1==true} cnumsup _ cnumsub;
dashes { kern.x = -@4.advancewidth + (@4.advancewidth - @1.advancewidth - @2.advancewidth - @3.advancewidth)/2; kern.y = 0m } / cnumsup {user1==true} cnumsup cnumsup _ cnumsub;

cnumsub { kern.x = -@2.advancewidth - (@1.advancewidth - @2.advancewidth)/2; kern.y = -100m;  } / dashes _ {user1==true};
cnumsub { kern.x = -@2.advancewidth - @3.advancewidth - (@1.advancewidth - @2.advancewidth - @3.advancewidth)/2; kern.y = -100m;  } / dashes _ cnumsub {user1==true};
cnumsub { kern.x = -@2.advancewidth - @3.advancewidth - @4.advancewidth - (@1.advancewidth - @2.advancewidth - @3.advancewidth -@4.advancewidth)/2; kern.y = -100m;  } / dashes _ cnumsub cnumsub {user1==true};

ANY { kern.x = (@1.advancewidth - @2.advancewidth)/2; kern.y = 100m } / dashes cnumsub {user1==true} _;
ANY { kern.x = (@1.advancewidth - @2.advancewidth - @3.advancewidth)/2; kern.y = 100m } / dashes cnumsub cnumsub {user1==true} _;
ANY { kern.x = (@1.advancewidth - @2.advancewidth - @3.advancewidth - @4.advancewidth)/2; kern.y = 100m } / dashes cnumsub cnumsub cnumsub {user1==true} _;
endif;

// kerning fix for fractions with old figures
slashold { kern.x = -175m } / p("slash") _;
slashold2 { kern.x = -115m } / p("slash") _;

// kerning fix for small capital variant A and diaeresis

//smallcap_salt_A_1 = u(0x00E0.. 0x00E5, 0x0103, 0x0105);
//smallcap_salt_A_2 = u(0x0300.. 0x0303, 0x0308, 0x030A, 0x0306, 0x0328);


///u(0x301 ){ shift.x = -130m; shift.y = -90m } / p("a.scalt") _;
///u(0x302 ){ shift.x = -180m; shift.y = -90m } / p("a.scalt") _;

///u(0x0308) { shift.x = -50m; shift.y = -10m } / p("a.scalt") _;
///u(0x030A) { shift.x = -120m; shift.y = -150m } / p("a.scalt") _;
///u(0x0306) { shift.x = -140m; shift.y = -50m } / p("a.scalt") _;
///u(0x0328) { shift.x = 250m; } / p("a.scalt") _;

///smallcap_salt_A_2 { shift.x = -150m; shift.y = -90m } / p("a.scalt") _;

//u(0x0306) { shift.x = -100; shift.y = -50 } / p("a.scalt") _;
//u(0x030A) { shift.x = -100; shift.y = -150 } / p("a.scalt") _;
//smallcap_salt_A_2 { shift.x = -100; shift.y = -90 } / p("a.scalt") _;


"""

feat_linlibBI = u"""
smcp {id = "smcp"; name.LG_USENG="'smcp' Small capitals";}
"""

feat=u"""
algn { id = "algn"; name.LG_USENG="'algn' Right aligned numbers or footnote numbering signs"; settings {
	none { value = 0; name.LG_USENG = "None"; }
	emlength { value = 1; name.LG_USENG = "Aligned for 1em length"; } 
	double { value = 2; name.LG_USENG = "Aligned for two characters"; } 
	triple { value = 3; name.LG_USENG = "Aligned for three characters"; } 
	quadruple { value = 4; name.LG_USENG = "Aligned for four characters"; } 

}}
arti { id = "arti"; default = 0; 
// name.LG_HU = string("'arti' Számok elé névelő");
name.LG_USENG = string ("'arti' Definitive article before numbers"); }

circ { id = "circ"; name.LG_USENG="'circ' Enclosed alphanumerics"; settings { 
	none { value = 0; name.LG_USENG = "None"; }
	circled { value = 1; name.LG_USENG = "Circled numbers and letters"; } 
	parenthesized { value = 2; name.LG_USENG = "Parenthesized numbers and letters"; } 
	negative { value = 3; name.LG_USENG = "White on black circled numbers"; } 
	double { value = 4; name.LG_USENG = "Double circled numbers"; } 
}}
dash { id="dash"; name.LG_USENG="'dash' N-dash correction"; }
dbls { id="dbls"; name.LG_USENG="'dbls' Double-struck capitals"; }
foot { id = "foot"; name.LG_USENG="'foot' Footnote numbering signs"; settings {
	none { value = 0; name.LG_USENG = "None"; }
	basic { value = 1; name.LG_USENG = "Asterisk, dagger, ..."; }
	double { value = 2; name.LG_USENG = "Asterisk, double asterisk, ..."; }
}}
frsp { id = "frsp"; name.LG_USENG = "'frsp' 1/8 em space before !, ?, : and ;"}
grkn { id = "grkn"; name.LG_USENG="'grkn' Numbers to Greek small letters"; }
hang { id = "hang"; name.LG_USENG="'hang' Hanging punctuation"; settings {
	none { value = 0; name.LG_USENG = "None"; }
	onlyhyphen { value = 1; name.LG_USENG = "Only inserted hyphen"; }
	all { value = 2; name.LG_USENG = "All hyphen, endash, emdash and punctuation."; }
}}

lng { id = "lng"; default = 0;
name.LG_USENG = string ("'lng' Language");
 settings { 
	none {value = 0; name.LG_USENG="None" }
	AFK { value = 27; name.LG_USENG="AFK" }
	AZE { value = 202; name.LG_USENG="AZE" }
	CAT { value = 37; name.LG_USENG="CAT"}
	CSY { value = 42; name.LG_USENG="CSY"}
	CRT { value = 203; name.LG_USENG="CRT"}
	DAN { value = 45; name.LG_USENG="DAN"}
	DEU { value = 49; name.LG_USENG="DEU"}
	ENG { value = 1; name.LG_USENG="ENG"}
	ELL { value = 30; name.LG_USENG="ELL"}
	EO { value = 200; name.LG_USENG="EO"}
	ESP { value = 34; name.LG_USENG="ESP"}
	FIN { value = 35; name.LG_USENG="FIN"}
	FRA { value = 33; name.LG_USENG="FRA"}
	HUN { value = 36; name.LG_USENG="HUN"}
	ITA { value = 39; name.LG_USENG="ITA"}
	LTZ { value = 201; name.LG_USENG="LTZ"}
	MOL { value = 230; name.LG_USENG="MOL"}
	NLD { value = 31; name.LG_USENG="NLD"}
	PLK { value = 48; name.LG_USENG="PLK"}
	PTG { value = 3; name.LG_USENG="PTG"}
	ROM { value = 40; name.LG_USENG="ROM"}
	RUS { value = 7; name.LG_USENG="RUS"}
	SRPL { value = 52; name.LG_USENG="SRPL"}
	SLV { value = 50; name.LG_USENG="SLV"}
	SRB { value = 51; name.LG_USENG="SRB"}
	SVE { value = 46; name.LG_USENG="SVE"}
	TRK { value = 90; name.LG_USENG="TRK"}
}}

minu {
	id = "minu";
	default = 1;
	name.LG_USENG = string ("'minu' Minus sign");
//	name.LG_HU = string ("'minu' Mínuszjel");
}
nfsp { id = "nfsp"; name.LG_USENG = "'nfsp' Non-French spacing"}
numt { id = "name"; default = 0;
//	name.LG_HU = string ("'name' Számokból számnevek");
	name.LG_USENG = string ("'name' Number names from numbers");
	settings {
		none {value = 0; name.LG_USENG = "None"}
		cardinal { value = 1; name.LG_USENG = "Cardinal number name"}
		ordinal { value = 2; name.LG_USENG = "Ordinal number name"}
		ordabbr { value = 3; name.LG_USENG = "Ordinal abbreviation"}
	}
}

quot { id="quot"; name.LG_USENG="'quot' Quoation mark correction"; }
texm { id = "texm"; 
//name.LG_HU = "'texm' TeX-mód";
name.LG_USENG = string ("'texm' TeX-mode"); }
thou {
	id = "thou";
	name.LG_USENG = string ("'thou' Thousand separation");
//	name.LG_HU = string ("'thou' Ezrestagolás");
	default = normal;
	settings {
		none { value = 0; name.LG_HU = string("Nincs"); name.LG_USENG = string("None"); }
		normal { value = 1; name.LG_HU = string("10000-től"); name.LG_USENG = string("From 10000"); }
		tab { value = 2; name.LG_HU = string("1000-től"); name.LG_USENG = string("From 1000"); }
	}
}

vari { id = "vari"; 
//name.LG_HU = "'vari' nyelvi variáns";
name.LG_USENG = string ("'vari' language variant"); }

"""

glyph=u"""

diaL = p("aacute", "adieresis", "eacute", "iacute", "oacute", "odieresis", "ohungarumlaut", "uacute", "udieresis", "uhungarumlaut", "Aacute", "Adieresis", "Adieresis.alt", "Eacute", "Iacute", "Oacute", "Odieresis", "Odieresis.alt", "Ohungarumlaut", "Udieresis", "Udieresis.alt", "Uacute", "Uhungarumlaut")
diaB = p("a", "a", "e", "dotlessi", "o", "o", "o", "u", "u", "u", "A", "A", "A", "E", "I", "O", "O", "O", "O", "U", "U", "U", "U")
diaD = p("acutecomb", "uni0308", "acutecomb", "acutecomb", "acutecomb", "uni0308", "uni030B", "acutecomb", "uni0308", "uni030B", "acute.cap", "dieresis.cap", "dieresis.cap", "acute.cap", "acute.cap", "acute.cap", "dieresis.cap", "dieresis.cap", "hungarumlaut.cap", "dieresis.cap", "dieresis.cap", "acute.cap", "hungarumlaut.cap")

// French spacing before !, ?, : and ;
french_punct = p("exclam", "question", "colon", "semicolon");
punct = (french_punct, p("comma", "period", "ellipsis", "parenright", "parenleft"));
punctsp = (punct, u(0x0020));
leftpunct = p("parenleft", "braceleft", "bracketleft", "space");
quots = p("quotedbl", "quotedblbase", "quotedblleft", "quotedblright");
sentenceend = p("exclam", "question", "period");

nonletter = (punctsp, quots, p("hyphen"), p("endash"), p("emdash"));

//thinspace = u(0x202F)
//thinspacelen = thinspace

// zero width space
ZWSP = u(0x200B);
SEPARATOR = u(0x005C);
// digit variants
d0 = u(0x0030);
d1 = u(0x0031);
d2 = u(0x0032);
d3 = u(0x0033);
d4 = u(0x0034);
d5 = u(0x0035);
d6 = u(0x0036);
d7 = u(0x0037);
d8 = u(0x0038);
d9 = u(0x0039);

dx = u(0x0031.. 0x0039);
dd = u(0x0030.. 0x0039);
// space, (, [, { and u(0x200B)
cmin = u(0x0020, 0x0028, 0x005B, 0x007B, 0x200B);
cdecsep = u(0x002C, 0x002E); // . and ,

slashold = p("four.oldstyle");
slashold2 = p("zero.oldstyle", "two.oldstyle", "three.oldstyle", "five.oldstyle", "seven.oldstyle", "nine.oldstyle");

"""

sub_linlibBI=u"""
if (smcp)
	csc1 > csc2;
endif;
"""

sub=u"""

if (frsp)
french_punct > @2 { u_frsp = 1 } / ^ ANY _ { u_frsp == 0 };
french_punct > u(0x200A) { u_frsp = 2 } u(0x200A) { u_frsp = 2 } u(0x200A) { u_frsp = 2 } @1 { u_frsp = 2 } / ^ _ { u_frsp == 0 };
endif;

// fix hard dotted line (used by OpenOffice.org TOC)

p("period") p("period") p("period") > _ _ p("ellipsis") / letters _ _ _;
//p("ellipsis") p("period") > p("period") p("period") p("period") p("period"); 

if (minu && !sups)
	u(0x002D) > u(0x2212) / cmin ^ _ dd; // after space or parenthesis
	u(0x002D) > @2 / ANY _ dd; // don't modify
	u(0x002D) > u(0x2212) / ^ _ dd; // at the beginning of the line
endif;

if (circ > 0)
if (circ == 1)
	dd > u(0x24EA, 0x2460.. 0x2468); // CHECK
	d1 dd > _ u(0x2469.. 0x2472); // CHECK
	d2 d0 > _ u(0x2473); // CHECK
	u(0x0041 .. 0x005A) > u(0x24B6.. 0x24CF); // CHECK
	u(0x0061 .. 0x007A) > u(0x24D0.. 0x24E9); // CHECK
endif;
if (circ == 2)
	dx > u(0x2474.. 0x247C); // CHECK
	d1 dd > _ u(0x247D.. 0x2486); // CHECK
	d2 d0 > _ u(0x2487); // CHECK
endif;
if (circ == 3)
	dd > u(0x24FF, 0x2776.. 0x277E); // CHECK
	d1 dd > _ u(0x277F, 0x24EB.. 0x24F3); // CHECK
	d2 d0 > _ u(0x24F4); // CHECK
endif;
if (circ == 4)
	dx > u(0x24F5.. 0x24FD); // CHECK
	d1 d0 > _ u(0x24FE); // CHECK
endif;
endif;

if (grkn)
dx > u(0x03B1.. 0x03B9); // CHECK
d1 dd > _ u(0x03BA.. 0x03C3); // CHECK
d2 u(0x0030.. 0x0035) > _ u(0x03C4.. 0x03C9); // CHECK
endif;

if (dbls)
diaL _ > diaB diaD$1 / ^ _ _;
endif;

if (texm)

// Greek letters

//u(0x005C) p("a") p("l") p("p") p("h") p("a") >  u(0x03B1) _ _ _ _ _;
//u(0x005C) p("b") p("e") p("t") p("a") 	> u(0x03B2):(1 5) _ _ _ _ ;
u(0x005C) p("a") p("l") p("p") p("h") p("a") >  u(0x03B1):(1 2 3 4 5 6) _ _ _ _ _;
u(0x005C) p("b") p("e") p("t") p("a") 	> u(0x03B2):(1 5) _ _ _ _ ;
u(0x005C) p("g") p("a") p("m") p("m") p("a") 	> _ _ _ _ _ u(0x03B3);
u(0x005C) p("d") p("e") p("l") p("t") p("a") 	> _ _ _ _ _ u(0x03B4);
u(0x005C) p("e") p("p") p("s") p("i") p("l") p("o") p("n") 	> _ _ _ _ _ _ _ _ u(0x03F5);
u(0x005C) p("v") p("a") p("r") p("e") p("p") p("s") p("i") p("l") p("o") p("n") 	> _ _ _ _ _ _ _ _ _ _ _ u(0x03B5);
u(0x005C) p("z") p("e") p("t") p("a") 	> _ _ _ _ u(0x03B6);
u(0x005C) p("e") p("t") p("a") 	> _ _ _ u(0x03B7);
u(0x005C) p("t") p("h") p("e") p("t") p("a") 	> _ _ _ _ _ u(0x03B8);
u(0x005C) p("v") p("a") p("r") p("t") p("h") p("e") p("t") p("a") 	> _ _ _ _ _ _ _ _ u(0x03D1);
u(0x005C) p("i") p("o") p("t") p("a") 	> _ _ _ _ u(0x03B9);
u(0x005C) p("k") p("a") p("p") p("p") p("a") 	> _ _ _ _ _ u(0x03BA);
u(0x005C) p("l") p("a") p("m") p("d") p("a") 	> _ _ _ _ _ u(0x03BB);
u(0x005C) p("m") p("u") 	> _ _ u(0x03BC);
u(0x005C) p("n") p("u") 	> _ _ u(0x03BD);
u(0x005C) p("x") p("i") 	> _ _ u(0x03BE);
u(0x005C) p("p") p("i") 	> _ _ u(0x03C0);
u(0x005C) p("v") p("a") p("r") p("p") p("i") 	> _ _ _ _ _ u(0x03D6);
u(0x005C) p("r") p("h") p("o") 	> _ _ _ u(0x03C1);
u(0x005C) p("v") p("a") p("r") p("r") p("h") p("o") 	> _ _ _ _ _ _ u(0x03F1);
u(0x005C) p("v") p("a") p("r") p("s") p("i") p("g") p("m") p("a") 	> _ _ _ _ _ _ _ _ u(0x03C2);
u(0x005C) p("s") p("i") p("g") p("m") p("a") 	> _ _ _ _ _ u(0x03C3);
u(0x005C) p("t") p("a") p("u") 	> _ _ _ _ u(0x03C4);
u(0x005C) p("u") p("p") p("s") p("i") p("l") p("o") p("n") 	> _ _ _ _ _ _ _ u(0x03C5);
u(0x005C) p("p") p("h") p("i") 	> _ _ _ u(0x03D5);
u(0x005C) p("v") p("a") p("r") p("p") p("h") p("i") 	> _ _ _ _ _ _ u(0x03C6);
u(0x005C) p("c") p("h") p("i") 	> _ _ _ u(0x03C7);
u(0x005C) p("p") p("s") p("i") 	> _ _ _ u(0x03C8);
u(0x005C) p("o") p("m") p("e") p("g") p("a") 	> _ _ _ _ _ _ u(0x03C9);
endif;

if (texm)
u(0x005C) p("G") p("a") p("m") p("m") p("a") 	> _ _ _ _ _ u(0x0393);
u(0x005C) p("D") p("e") p("l") p("t") p("a") 	> _ _ _ _ _ u(0x0394);
u(0x005C) p("T") p("h") p("e") p("t") p("a") 	> _ _ _ _ _ u(0x0398);
u(0x005C) p("L") p("a") p("m") p("d") p("a") 	> _ _ _ _ _ u(0x039B);
u(0x005C) p("X") p("i") 	> _ _ u(0x039E);
u(0x005C) p("P") p("i") 	> _ _ u(0x03A0);
u(0x005C) p("S") p("i") p("g") p("m") p("a") 	> _ _ _ _ _ u(0x03A3);
u(0x005C) p("U") p("p") p("s") p("i") p("l") p("o") p("n") 	> _ _ _ _ _ _ _ u(0x03A5);
u(0x005C) p("P") p("h") p("i") 	> _ _ _ u(0x03A6);
u(0x005C) p("P") p("s") p("i") 	> _ _ _ u(0x03A8);
u(0x005C) p("O") p("m") p("e") p("g") p("a") 	> _ _ _ _ _ u(0x03A9);

// other symbols

u(0x005C) p("p") p("m") > _ _ u(0x00B1);
u(0x005C) p("m") p("p") > _ _ u(0x2213);
u(0x005C) p("t") p("i") p("m") p("e") p("s") > _ _ _ _ _ u(0x00D7);
u(0x005C) p("s") p("e") p("t") p("m") p("i") p("n") p("u") p("s") > _ _ _ _ _ _ _ _ u(0x2216);
u(0x005C) p("c") p("a") p("p") > _ _ _ u(0x2229);
u(0x005C) p("c") p("u") p("p") > _ _ _ u(0x222A);
u(0x005C) p("w") p("e") p("d") p("g") p("e") > _ _ _ _ _ u(0x2227);
u(0x005C) p("v") p("e") p("e") > _ _ _ u(0x2228);
//u(0x005C) p("w") p("e") p("d") p("g") p("e") > _ _ _ _ _ u(0x2227):(1 2 3 4 5);
//u(0x005C) p("v") p("e") p("e") > _ _ _ u(0x2228):(1 2 3);
u(0x005C) p("l") p("e") p("q") > _ _ _ u(0x2264);
u(0x005C) p("g") p("e") p("q") > _ _ _ u(0x2265);
u(0x005C) p("l") p("e") > _ _ u(0x2264);
u(0x005C) p("g") p("e") > _ _ u(0x2265);
u(0x005C) p("n") p("o") p("t") u(0x005C) p("l") p("e") > _ _ _ _ _ _ u(0x2270);
u(0x005C) p("n") p("o") p("t") u(0x005C) p("g") p("e") > _ _ _ _ _ _ u(0x2271);
u(0x005C) p("l") p("l") > _ _ u(0x226A);
endif;

if (texm)
u(0x005C) p("g") p("g") > _ _ u(0x226B);
u(0x005C) p("n") p("e") p("q") > _ _ _ u(0x2260);
u(0x005C) p("i") p("n") > _ _ u(0x2208);
u(0x005C) p("n") p("o") p("t") u(0x005C) p("i") p("n") > _ _ _ _ _ _ u(0x2209);
u(0x005C) p("n") p("i") > _ _ u(0x220B);
u(0x005C) p("n") p("o") p("t") u(0x005C) p("n") p("i") > _ _ _ _ _ _ u(0x220C);
u(0x005C) p("s") p("u") p("b") p("s") p("e") p("t") > _ _ _ _ _ _ u(0x2282);
u(0x005C) p("s") p("u") p("p") p("s") p("e") p("t") > _ _ _ _ _ _ u(0x2283);
u(0x005C) p("n") p("o") p("t") u(0x005C) p("s") p("u") p("b") p("s") p("e") p("t") > _ _ _ _ _ _ _ _ _ _ u(0x2284);
u(0x005C) p("n") p("o") p("t") u(0x005C) p("s") p("u") p("p") p("s") p("e") p("t") > _ _ _ _ _ _ _ _ _ _ u(0x2285);
u(0x005C) p("s") p("i") p("m") > _ _ _ u(0x223C);
u(0x005C) p("n") p("s") p("i") p("m") > _ _ _ _ u(0x2241);
u(0x005C) p("a") p("p") p("p") p("r") p("o") p("x") > _ _ _ _ _ _ u(0x2248);
u(0x005C) p("m") p("i") p("d") > _ _ _ u(0x2223);
u(0x005C) p("n") p("m") p("i") p("d") > _ _ _ _ u(0x2224);
u(0x005C) u(0x007C) > _ u(0x2225);
u(0x005C) p("n") p("o") p("t") u(0x003C) > _ _ _ _ u(0x226E);
u(0x005C) p("n") p("o") p("t") u(0x003E) > _ _ _ _ u(0x226F);
u(0x005C) p("p") p("a") p("r") p("a") p("l") p("l") p("e") p("l") > _ _ _ _ _ _ _ _ u(0x2225);
u(0x005C) p("n") p("o") p("t") u(0x005C) u(0x007C) > _ _ _ _ _ u(0x2226);
u(0x005C) p("n") p("p") p("a") p("r") p("a") p("l") p("l") p("e") p("l") > _ _ _ _ _ _ _ _ _ u(0x2226);

u(0x005C) p("g") p("e") p("t") p("s") > _ _ _ _ u(0x2190);
u(0x005C) p("l") p("e") p("f") p("t") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ _ _ u(0x2190);
u(0x005C) p("u") p("p") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ u(0x2191);
u(0x005C) p("r") p("i") p("g") p("h") p("t") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ _ _ _ u(0x2192);
u(0x005C) p("t") p("o") > _ _ u(0x2192);
u(0x005C) p("d") p("o") p("w") p("n") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ _ _ u(0x2193);
u(0x005C) p("l") p("e") p("f") p("t") p("r") p("i") p("g") p("h") p("t") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ _ _ _ _ _ _ _ u(0x2194);
endif;

if (texm)
u(0x005C) p("L") p("e") p("f") p("t") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ _ _ u(0x21D0);
u(0x005C) p("U") p("p") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ u(0x21D1);
u(0x005C) p("R") p("i") p("g") p("h") p("t") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ _ _ _ u(0x21D2);
u(0x005C) p("D") p("o") p("w") p("n") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ _ _ u(0x21D3);
u(0x005C) p("L") p("e") p("f") p("t") p("r") p("i") p("g") p("h") p("t") p("a") p("r") p("r") p("o") p("w") > _ _ _ _ _ _ _ _ _ _ _ _ _ _ u(0x21D4);

u(0x005C) p("h") p("b") p("a") p("r") > _ _ _ _ u(0x210F);
u(0x005C) p("R") p("e") > _ _ u(0x211C);
u(0x005C) p("I") p("m") > _ _ u(0x2111);
u(0x005C) p("e") p("l") p("l") > _ _ _ u(0x2113);
u(0x005C) p("a") p("l") p("e") p("p") p("h") > _ _ _ _ _ u(0x2135);
u(0x005C) p("t") p("r") p("i") p("a") p("n") p("g") p("l") p("e") > _ _ _ _ _ _ _ _ u(0x2206);
u(0x005C) p("i") p("n") p("f") p("t") p("y") > _ _ _ _ _ u(0x221E);
u(0x005C) p("p") p("a") p("r") p("t") p("i") p("a") p("l") > _ _ _ _ _ _ _ u(0x2202);


u(0x005C) p("s") p("u") p("r") p("d") > _ _ _ _ u(0x221A);
u(0x005C) p("s") p("u") p("m") > _ _ _ u(0x2211);
u(0x005C) p("i") p("n") p("t") > _ _ _ u(0x222B);

u(0x005C) p("p") p("r") p("o") p("d") > _ _ _ _ u(0x220F);
u(0x005C) p("p") p("r") p("i") p("m") p("e") > _ _ _ _ _ u(0x2032);

u(0x005C) p("a") p("n") p("g") p("l") p("e") > _ _ _ _ _ u(0x2220);
u(0x005C) p("p") p("e") p("r") p("p") > _ _ _ _ u(0x27C2);
u(0x005C) p("i") p("i") p("n") p("t") > _ _ _ _ u(0x222C);
u(0x005C) p("i") p("i") p("i") p("n") p("t") > _ _ _ _ _ u(0x222D);
u(0x005C) p("o") p("i") p("n") p("t") > _ _ _ _ u(0x222E);


u(0x005C) p("e") p("m") p("p") p("t") p("y") p("s") p("e") p("t") > _ _ _ _ _ _ _ _ u(0x2205);
u(0x005C) p("f") p("o") p("r") p("a") p("l") p("l") > _ _ _ _ _ _ u(0x2200);
u(0x005C) p("e") p("x") p("i") p("s") p("t") p("s") > _ _ _ _ _ _ u(0x2203);
endif;

if (numt == 1 || numt == 2)

	SEPARATOR > _;

// removing left zeros

	csc123ligdash u(0x200B) d0 u(0x200B) > @1 / ^_ _ _ _;
	csc123ligdash u(0x200B) d0 d0 u(0x200B) > @1 u(0x200B) / ^_ _ _ _ _;
	csc123ligdash u(0x200B) d0 dd u(0x200B) > @1 u(0x200B) @4 u(0x200B) / ^_ _ _ _ _;
	csc123ligdash u(0x200B) d0 dd dd u(0x200B) > @1 u(0x200B) @4 @5 u(0x200B) / ^_ _ _ _ _ _;
	csc123ligdash u(0x200B) d0 dd dd dd u(0x200B) > @1 u(0x200B) @4 @5 @6 u(0x200B) / ^_ _ _ _ _ _ _;
	csc123ligdash u(0x200B) d0 dd dd dd dd u(0x200B) > @1 u(0x200B) @4 @5 @6 @7 u(0x200B) / ^_ _ _ _ _ _ _ _;
	csc123ligdash u(0x200B) d0 dd dd dd dd dd u(0x200B) > @1 u(0x200B) @4 @5 @6 @7 @8 u(0x200B) / ^_ _ _ _ _ _ _ _ _;
	csc123ligdash u(0x200B) d0 dd dd dd dd dd dd u(0x200B) > @1 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _;
	csc123ligdash u(0x200B) d0 dd dd dd dd dd dd dd u(0x200B) > @1 u(0x200B) @4 @5 @6 @7 @8 @9 @10 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _;
	csc123ligdash u(0x200B) d0 dd dd dd dd dd dd dd dd u(0x200B) > @1 u(0x200B) @4 @5 @6 @7 @8 @9 @10 @11 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _ _;

	u(0x200B) d0 u(0x200B) > _ / ^_ _ _ ;
	u(0x200B) d0 d0 u(0x200B) > u(0x200B) / ^_ _ _ _;
	u(0x200B) d0 dd u(0x200B) > u(0x200B) @3 u(0x200B) / ^_ _ _ _;
	u(0x200B) d0 dd dd u(0x200B) > u(0x200B) @3 @4 u(0x200B) / ^_ _ _ _ _;
	u(0x200B) d0 dd dd dd u(0x200B) > u(0x200B) @3 @4 @5 u(0x200B) / ^_ _ _ _ _ _;
	u(0x200B) d0 dd dd dd dd u(0x200B) > u(0x200B) @3 @4 @5 @6 u(0x200B) / ^_ _ _ _ _ _ _;
	u(0x200B) d0 dd dd dd dd dd u(0x200B) > u(0x200B) @3 @4 @5 @6 @7 u(0x200B) / ^_ _ _ _ _ _ _ _;
	u(0x200B) d0 dd dd dd dd dd dd u(0x200B) > u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_ _ _ _ _ _ _ _ _;
	u(0x200B) d0 dd dd dd dd dd dd dd u(0x200B) > u(0x200B) @3 @4 @5 @6 @7 @8 @9 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _;
	u(0x200B) d0 dd dd dd dd dd dd dd dd u(0x200B) > u(0x200B) @3 @4 @5 @6 @7 @8 @9 @10 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _;

	// optional space
	u(0x003A) u(0x003A) d0 u(0x200B) > u(0x200B) / ^_ _ _ _;
	u(0x003A) u(0x003A) dd u(0x200B) > u(0x0020) u(0x200B) / ^_ _ _ _;
	u(0x003A) u(0x003A) d0 d0 u(0x200B) > u(0x200B) / ^_ _ _ _ _;
	u(0x003A) u(0x003A) dd dd u(0x200B) > u(0x0020) u(0x200B) / ^_ _ _ _ _;
	u(0x003A) u(0x003A) d0 d0 d0 u(0x200B) > u(0x200B) / ^_ _ _ _ _ _;
	u(0x003A) u(0x003A) dd dd dd u(0x200B) > u(0x0020) u(0x200B) / ^_ _ _ _ _ _;
	u(0x003A) u(0x003A) d0 d0 d0 d0 d0 d0 u(0x200B) > u(0x200B) / ^_ _ _ _ _ _ _ _ _;
	u(0x003A) u(0x003A) dd dd dd dd dd dd u(0x200B) > u(0x0020) u(0x200B) / ^_ _ _ _ _ _ _ _ _;

// Hungarian numerals
if (numt > 0 && lng == HUN)

	if (arti)
	u(0x200B) u(0x200B) (d1, d5) u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 u(0x200B) / ^_ _ _ _;
	u(0x200B) u(0x200B) dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 u(0x200B) / ^_ _ _ _;
	u(0x200B) u(0x200B) d5 dd u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 @4 u(0x200B) / ^_ _ _ _ _;
	u(0x200B) u(0x200B) dd dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 @4 u(0x200B) / ^_ _ _ _ _;
	u(0x200B) u(0x200B) d5 dd dd u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 @4 @5 u(0x200B) / ^_ _ _ _ _ _;
	u(0x200B) u(0x200B) dd dd dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 @4 @5 u(0x200B) / ^_ _ _ _ _ _;
	u(0x200B) u(0x200B) (d1, d5) dd dd dd u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 @4 @5 @6 u(0x200B) / ^_ _ _ _ _ _ _;
	u(0x200B) u(0x200B) dd dd dd dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 @4 @5 @6 u(0x200B) / ^_ _ _ _ _ _ _;
	u(0x200B) u(0x200B) d5 dd dd dd dd u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 u(0x200B) / ^_ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) dd dd dd dd dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 u(0x200B) / ^_ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) d5 dd dd dd dd dd u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_ _ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) dd dd dd dd dd dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_ _ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) (d1, d5) dd dd dd dd dd dd u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 @8 @9 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) dd dd dd dd dd dd dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 @8 @9 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) d5 dd dd dd dd dd dd dd u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 @8 @9 @10 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) dd dd dd dd dd dd dd dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 @8 @9 @10 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) d5 dd dd dd dd dd dd dd dd u(0x200B) > p("a") p("z") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 @8 @9 @10 @11 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _ _;
	u(0x200B) u(0x200B) dd dd dd dd dd dd dd dd dd u(0x200B) > p("a") u(0x0020) u(0x200B) @3 @4 @5 @6 @7 @8 @9 @10 @11 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _ _;
	endif;

if (numt == 2 && lng == HUN)
	u(0x200B) d0 u(0x200B) u(0x200B) > p("n") p("u") p("l") p("l") p("a") p("d") p("i") p("k") / ^_ _ _ _;
	csc123ligdash u(0x200B) d1 u(0x200B) u(0x200B) > @1 p("e") p("g") p("y") p("e") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) d1 u(0x200B) u(0x200B) > p("e") p("l") p("s") u(0x0151) / ^_ _ _ _;
	u(0x200B) d2 u(0x200B) u(0x200B) > p("m") u(0x00E1) p("s") p("o") p("d") p("i") p("k") / ^_ _ _ _;
	csc123ligdash u(0x200B) d2 u(0x200B) u(0x200B) > @1 p("k") p("e") p("t") p("t") p("e") p("d") p("i") p("k")  / ^_ _ _ _ _;
	u(0x200B) d3 u(0x200B) u(0x200B) > p("h") p("a") p("r") p("m") p("a") p("d") p("i") p("k") / ^_ _ _ _;
	u(0x200B) d4 u(0x200B) u(0x200B) > p("n") p("e") p("g") p("y") p("e") p("d") p("i") p("k") / ^_ _ _ _;
	u(0x200B) d5 u(0x200B) u(0x200B) > u(0x00F6) p("t") u(0x00F6) p("d") p("i") p("k") / ^_ _ _ _;
	u(0x200B) d6 u(0x200B) u(0x200B) > p("h") p("a") p("t") p("o") p("d") p("i") p("k") / ^_ _ _ _;
	u(0x200B) d7 u(0x200B) u(0x200B) > p("h") p("e") p("t") p("e") p("d") p("i") p("k") / ^_ _ _ _;
	u(0x200B) d8 u(0x200B) u(0x200B) > p("n") p("y") p("o") p("l") p("c") p("a") p("d") p("i") p("k") / ^_ _ _ _;
	u(0x200B) d9 u(0x200B) u(0x200B) > p("k") p("i") p("l") p("e") p("n") p("c") p("e") p("d") p("i") p("k") / ^_ _ _ _;
	u(0x200B) d1 d0 u(0x200B) u(0x200B) > p("t") p("i") p("z") p("e") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) d2 d0 u(0x200B) u(0x200B) > p("h") p("u") p("s") p("z") p("a") p("d") p("i") p("k") / ^_ _ _ _ _;

	u(0x200B) d3 d0 u(0x200B) u(0x200B) > p("h") p("a") p("r") p("m") p("i") p("n") p("c") p("a") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) d4 d0 u(0x200B) u(0x200B) > p("n") p("e") p("g") p("y") p("v") p("e") p("n") p("e") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) d5 d0 u(0x200B) u(0x200B) > u(0x00F6) p("t") p("v") p("e") p("n") p("e") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) d6 d0 u(0x200B) u(0x200B) > p("h") p("a") p("t") p("v") p("a") p("n") p("a") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) d7 d0 u(0x200B) u(0x200B) > p("h") p("e") p("t") p("v") p("e") p("n") p("e") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) d8 d0 u(0x200B) u(0x200B) > p("n") p("y") p("o") p("l") p("c") p("v") p("a") p("n") p("a") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) d9 d0 u(0x200B) u(0x200B) > p("k") p("i") p("l") p("e") p("n") p("c") p("v") p("e") p("n") p("e") p("d") p("i") p("k") / ^_ _ _ _ _;

	u(0x200B) (d3, d6, d8) d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("a") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) dx d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("e") p("d") p("i") p("k") / ^_ _ _ _ _;
	u(0x200B) dx d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("a") p("d") p("i") p("k") / ^_ _ _ _ _ _;
	u(0x200B) d1 d0 d0 d0 u(0x200B) u(0x200B) > p("e") p("z") p("r") p("e") p("d") p("i") p("k") / ^_ _ _ _ _ _ _;
	u(0x200B) dx d0 d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 u(0x200B) p("e") p("z") p("r") p("e") p("d") p("i") p("k") / ^_ _ _ _ _ _ _;
	u(0x200B) dx dd d0 d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("e") p("z") p("r") p("e") p("d") p("i") p("k") / ^_ _ _ _ _ _ _ _;
	u(0x200B) dx dd dd d0 d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("e") p("z") p("r") p("e") p("d") p("i") p("k") / ^_ _ _ _ _ _ _ _ _;
endif;

	u(0x200B) d0 u(0x200B) u(0x200B) > p("n") p("u") p("l") p("l") p("a") / ^_ _ _ _;
	u(0x200B) d1 u(0x200B) > p("e") p("g") p("y") / ^_ _ _;
	u(0x200B) d2 u(0x200B) u(0x200B) > p("k") p("e") p("t") p("t") u(0x0151) / ^_ _ _ _;
	u(0x200B) d2 u(0x200B) > p("k") u(0x00E9) p("t") / ^_ _ _;
	u(0x200B) d3 u(0x200B) > p("h") u(0x00E1) p("r") p("o") p("m") / ^_ _ _;
	u(0x200B) d4 u(0x200B) > p("n") u(0x00E9) p("g") p("y") / ^_ _ _;
	u(0x200B) d5 u(0x200B) > u(0x00F6) p("t") / ^_ _ _;
	u(0x200B) d6 u(0x200B) > p("h") p("a") p("t") / ^_ _ _;
	u(0x200B) d7 u(0x200B) > p("h") u(0x00E9) p("t") / ^_ _ _;
	u(0x200B) d8 u(0x200B) > p("n") p("y") p("o") p("l") p("c") / ^_ _ _;
	u(0x200B) d9 u(0x200B) > p("k") p("i") p("l") p("e") p("n") p("c") / ^_ _ _;

	u(0x200B) d1 d0 u(0x200B) > p("t") u(0x00ED) p("z") / ^_ _ _ _;
	u(0x200B) d1 dx u(0x200B) > p("t") p("i") p("z") p("e") p("n") u(0x200B) @3 u(0x200B) / ^_ _ _ _;
	u(0x200B) d2 d0 u(0x200B) > p("h") u(0x00FA) p("s") p("z") / ^_ _ _ _;
	u(0x200B) d2 dx u(0x200B) > p("h") p("u") p("s") p("z") p("o") p("n") u(0x200B) @3 u(0x200B) / ^_ _ _ _;
	u(0x200B) d3 d0 u(0x200B) > p("h") p("a") p("r") p("m") p("i") p("n") p("c") u(0x200B) / ^_ _ _ _;

	u(0x200B) d4 d0 u(0x200B) > p("n") p("e") p("g") p("y") p("v") p("e") p("n") u(0x200B) / ^_ _ _ _;
	u(0x200B) (d5, d9) d0 u(0x200B) > u(0x200B) @2 u(0x200B) p("v") p("e") p("n") u(0x200B) / ^_ _ _ _;
	u(0x200B) (d6, d8) d0 u(0x200B) > u(0x200B) @2 u(0x200B) p("v") p("a") p("n") u(0x200B) / ^_ _ _ _;
	u(0x200B) d7 d0 u(0x200B) > p("h") p("e") p("t") p("v") p("e") p("n") u(0x200B) / ^_ _;
	u(0x200B) dx dx u(0x200B) > u(0x200B) @2 d0 u(0x200B) @3 u(0x200B) / ^_;

	// separator
	u(0x003A) d0 d0 d0 u(0x200B) > _ _ _ _ u(0x200B);
	u(0x003A) dd dd dd u(0x200B) > _ _ _ _ u(0x002D) u(0x200B);
	u(0x003A) d0 d0 d0 d0 d0 d0 u(0x200B) > _ _ _ _ _ _ _ u(0x200B);
	u(0x003A) dd dd dd dd dd dd u(0x200B) > _ _ _ _ _ _ u(0x002D) u(0x200B);
	u(0x003A) d0 d0 d0 d0 d0 d0 d0 d0 d0 u(0x200B) > _ _ _ _ _ _ _ _ _ _ u(0x200B);
	u(0x003A) dd dd dd dd dd dd dd dd dd u(0x200B) > _ _ _ _ _ _ _ _ _ u(0x002D) u(0x200B);

	u(0x200B) d1 dd dd u(0x200B) > p("s") p("z") u(0x00E1) p("z") u(0x200B) @3 @4 u(0x200B) / ^_ _ _ _ _;
	u(0x200B) dx dd dd u(0x200B) > u(0x200B) @2 u(0x200B) p("s") p("z") u(0x00E1) p("z") u(0x200B) @3 @4 u(0x200B) / ^_ _ _ _ _;
	u(0x200B) d1 dd dd dd u(0x200B) > p("e") p("z") p("e") p("r") u(0x200B) @3 @4 @5 u(0x200B) / ^_ _ _ _ _ _;
	u(0x200B) dx d0 d0 d0 u(0x200B) > u(0x200B) @2 u(0x200B) p("e") p("z") p("e") p("r") / ^_ _ _ _ _ _;
	u(0x200B) dx dd dd dd u(0x200B) > u(0x200B) @2 u(0x200B) p("e") p("z") p("e") p("r") u(0x002D) u(0x200B) @3 @4 @5 u(0x200B) / ^_ _ _ _ _ _;
	u(0x200B) dx dd d0 d0 d0 u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("e") p("z") p("e") p("r") / ^_ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("e") p("z") p("e") p("r") u(0x002D) u(0x200B) @4 @5 @6 u(0x200B) / ^_ _ _ _ _ _ _;
	u(0x200B) dx dd dd d0 d0 d0 u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("e") p("z") p("e") p("r") / ^_ _ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd dd u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("e") p("z") p("e") p("r") u(0x002D) u(0x200B) @5 @6 @7 u(0x200B) / ^_ _ _ _ _ _ _ _;
	u(0x200B) dx d0 d0 d0 d0 d0 d0 u(0x200B) > u(0x200B) @2 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00F3) / ^_ _ _ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd dd dd u(0x200B) > u(0x200B) @2 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00F3) u(0x002D) u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_ _ _ _ _ _ _ _ _;
	u(0x200B) dx dd d0 d0 d0 d0 d0 d0 u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00F3) / ^_ _ _ _ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00F3) u(0x002D) u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _;
//	u(0x200B) dx dd dd d0 d0 d0 d0 d0 d0 u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00F3) / ^_ _ _ _ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00F3) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd dd dd dd dd dd u(0x200B) > u(0x200B) @2 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00E1) p("r") p("d") u(0x003A) @3 @4 @5 @6 @7 @8 @9 @10 @11 u(0x200B) @3 @4 @5 @6 @7 @8 @9 @10 @11 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd dd dd dd dd dd dd u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00E1) p("r") p("d") u(0x003A) @4 @5 @6 @7 @8 @9 @10 @11 @12 u(0x200B) @4 @5 @6 @7 @8 @9 @10 @11 @12 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd dd dd dd dd dd dd dd u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("m") p("i") p("l") p("l") p("i") u(0x00E1) p("r") p("d") u(0x003A) @4 @5 @6 @7 @8 @9 @10 @11 @12 u(0x200B) @4 @5 @6 @7 @8 @9 @10 @11 @12 u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _ _;

endif;
// English numerals
if (numt > 0 && lng == ENG)

if (numt == 2)
	u(0x200B) d0 u(0x200B) u(0x200B) > p("z") p("e") p("r") p("o") p("t") p("h") / ^_ _ _;
	u(0x200B) d1 u(0x200B) u(0x200B) > p("f") p("i") p("r") p("s") p("t") / ^_ _ _;
	u(0x200B) d2 u(0x200B) u(0x200B) > p("s") p("e") p("c") p("o") p("n") p("d") / ^_ _ _ _;
	u(0x200B) d3 u(0x200B) u(0x200B) > p("t") p("h") p("i") p("r") p("d") / ^_ _ _ _;
	u(0x200B) d5 u(0x200B) u(0x200B) > p("f") p("i") p("f") p("t") p("h") / ^_ _ _ _;
	u(0x200B) d8 u(0x200B) u(0x200B) > u(0x200B) d8 u(0x200B) p("h") / ^_ _ _ _;
	u(0x200B) d9 u(0x200B) u(0x200B) > p("n") p("i") p("n") p("t") p("h") / ^_ _ _ _;
	u(0x200B) dd u(0x200B) u(0x200B) > u(0x200B) @2 u(0x200B) p("t") p("h") / ^_ _ _ _;
	u(0x200B) d1 d2 u(0x200B) u(0x200B) > p("t") p("w") p("e") p("l") p("f") p("t") p("h") / ^_ _ _ _ _;
	u(0x200B) dx d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("t") p("h") / ^_ _ _ _ _;
	d0 d0 d0 u(0x200B) u(0x200B) > @1 @2 @3 u(0x200B) p("t") p("h") / ^_ _ _ _ _;
	u(0x200B) d1 dd u(0x200B) u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("t") p("h") / ^_ _ _ _ _;
	p("y") u(0x200B) u(0x200B) > p("i") p("e") p("t") p("h") / ^_ _ _;
endif;

	u(0x200B) d0 u(0x200B) u(0x200B) > p("z") p("e") p("r") p("o") / ^_ _ _;
	u(0x200B) d1 u(0x200B) > p("o") p("n") p("e") / ^_ _ _;
	u(0x200B) d2 u(0x200B) > p("t") p("w") p("o") / ^_ _ _;
	u(0x200B) d3 u(0x200B) > p("t") p("h") p("r") p("e") p("e") / ^_ _ _;
	u(0x200B) d4 u(0x200B) > p("f") p("o") p("u") p("r") / ^_ _ _;
	u(0x200B) d5 u(0x200B) > p("f") p("i") p("v") p("e") / ^_ _ _;
	u(0x200B) d6 u(0x200B) > p("s") p("i") p("x") / ^_ _ _;
	u(0x200B) d7 u(0x200B) > p("s") p("e") p("v") p("e") p("n") / ^_ _ _;
	u(0x200B) d8 u(0x200B) > p("e") p("i") p("g") p("h") p("t") / ^_ _ _;
	u(0x200B) d9 u(0x200B) > p("n") p("i") p("n") p("e") / ^_ _ _;
	u(0x200B) d1 d0 u(0x200B) > p("t") p("e") p("n") / ^_ _ _ _;
	u(0x200B) d1 d1 u(0x200B) > p("e") p("l") p("e") p("v") p("e") p("n") / ^_ _ _ _;
	u(0x200B) d1 d2 u(0x200B) > p("t") p("w") p("e") p("l") p("v") p("e") / ^_ _ _ _;
	u(0x200B) d1 d3 u(0x200B) > p("t") p("h") p("i") p("r") p("t") p("e") p("e") p("n") / ^_ _ _ _;
	u(0x200B) d1 d5 u(0x200B) > p("f") p("i") p("f") p("t") p("e") p("e") p("n") / ^_ _ _ _;
	u(0x200B) d1 d8 u(0x200B) > u(0x200B) @3 u(0x200B) p("e") p("e") p("n") / ^_ _ _ _;
	u(0x200B) d1 dx u(0x200B) > u(0x200B) @3 u(0x200B) p("t") p("e") p("e") p("n") / ^_ _ _ _;
	u(0x200B) d2 d0 u(0x200B) > p("t") p("w") p("e") p("n") p("t") p("y") u(0x200B) / ^_ _ _ _;
	u(0x200B) d3 d0 u(0x200B) > p("t") p("h") p("i") p("r") p("t") p("y") u(0x200B) / ^_ _ _ _;
	u(0x200B) d4 d0 u(0x200B) > p("f") p("o") p("r") p("t") p("y") u(0x200B) / ^_ _ _ _;
	u(0x200B) d5 d0 u(0x200B) > p("f") p("i") p("f") p("t") p("y") u(0x200B) / ^_ _ _ _;
	u(0x200B) d8 d0 u(0x200B) > u(0x200B) d8 u(0x200B) p("y") u(0x200B) / ^_ _ _ _;
	u(0x200B) dx d0 u(0x200B) > u(0x200B) @2 u(0x200B) p("t") p("y") u(0x200B) / ^_ _ _ _;
	u(0x200B) dx dx u(0x200B) > u(0x200B) @2 d0 u(0x200B) u(0x002D) u(0x200B) @3 u(0x200B) / ^_ _ _ _;

	// separator
	u(0x003A) d0 d0 u(0x200B) > _ _ _ u(0x200B); // one million
	if (vari == 0) 
	u(0x003A) dd dd u(0x200B) > u(0x0020) p("a") p("n") p("d") u(0x0020) u(0x200B) / ^_ _ _ _; // one million and one
	u(0x003A) d0 d0 d0 u(0x200B) > _ _ _ _ u(0x200B); // one million
	u(0x003A) d0 dd dd u(0x200B) > u(0x0020) p("a") p("n") p("d") u(0x0020) u(0x200B) / ^_ _ _ _ _; // one million and ten
	u(0x003A) dd dd dd u(0x200B) > _ _ u(0x002C) u(0x0020) u(0x200B); // one million, one thousand
	else
	u(0x003A) dd dd u(0x200B) > _ _ u(0x0020) u(0x200B);
	u(0x003A) dd dd dd u(0x200B) > _ _ _ u(0x0020) u(0x200B); // Two Thousand Ten
	endif;

	u(0x200B) dx dd dd u(0x200B) > u(0x200B) @2 u(0x200B) u(0x0020) p("h") p("u") p("n") p("d") p("r") p("e") p("d") u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_ _ _ _ _;
	u(0x200B) dx dx dd dd u(0x200B) > u(0x200B) @2 u(0x200B) u(0x0020) p("t") p("h") p("o") p("u") p("s") p("a") p("n") p("d") u(0x0020) u(0x200B) @3 @4 @5 u(0x200B) / ^_ _ _ _ _ _;
	u(0x200B) dx dd dd dd u(0x200B) > u(0x200B) @2 u(0x200B) u(0x0020) p("t") p("h") p("o") p("u") p("s") p("a") p("n") p("d") u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_ _ _ _ _ _;
	u(0x200B) dx dd dx dd dd u(0x200B) > u(0x200B) @2 @3 u(0x200B) u(0x0020) p("t") p("h") p("o") p("u") p("s") p("a") p("n") p("d") u(0x0020) u(0x200B) @4 @5 @6 u(0x200B) / ^_ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd u(0x200B) > u(0x200B) @2 @3 u(0x200B) u(0x0020) p("t") p("h") p("o") p("u") p("s") p("a") p("n") p("d") u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_ _ _ _ _ _ _;
	u(0x200B) dx dd dd dd dd dd u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) u(0x0020) p("t") p("h") p("o") p("u") p("s") p("a") p("n") p("d") u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_ _ _ _ _ _ _;

	u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("i") p("o") p("n") u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
	u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("i") p("o") p("n")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
	u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("i") p("o") p("n")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;

endif;
// German numerals
if (numt > 0 && lng == DEU)

	u(0x200B) d1 u(0x200B) > p("e") p("i") p("n") / ^_ _ _ csc123ligdash;

if (numt == 2)
	u(0x200B) d0 u(0x200B) u(0x200B) > p("n") p("u") p("l") p("l") p("t") p("e") / ^_ _ _ _;
	u(0x200B) d1 u(0x200B) u(0x200B) > p("e") p("r") p("s") p("t") p("e") / ^_ _ _ _;
	u(0x200B) d3 u(0x200B) u(0x200B) > p("d") p("r") p("i") p("t") p("t") p("e") / ^_ _ _ _;
	u(0x200B) d7 u(0x200B) u(0x200B) > p("s") p("i") p("e") p("b") p("t") p("e") / ^_ _ _ _;
	u(0x200B) d8 u(0x200B) u(0x200B) > p("a") p("c") p("h") p("t") p("e") / ^_ _ _ _;
	u(0x200B) dx u(0x200B) u(0x200B) > u(0x200B) @2 u(0x200B) p("t") p("e") / ^_ _ _ _;

	u(0x200B) d1 dd u(0x200B) u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("t") p("e") / ^_ _ _ _ _;
	u(0x200B) dx dd u(0x200B) u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("s") p("t") p("e") / ^_ _ _ _ _;
	u(0x200B) dx d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("t") p("e") / ^_ _ _ _ _ _;
	u(0x200B) dx d0 d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 @4 @5 u(0x200B) p("t") p("e") / ^_ _ _ _ _ _ _;
	u(0x200B) dd dd d0 d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 @4 @5 @6 u(0x200B) p("t") p("e") / ^_ _ _ _ _ _ _ _;
	u(0x200B) dd dd dd d0 d0 d0 u(0x200B) u(0x200B) > u(0x200B) @2 @3 @4 @5 @6 @7 u(0x200B) p("t") p("e") / ^_ _ _ _ _ _ _ _ _;
endif;

	u(0x200B) d0 u(0x200B) u(0x200B) > p("n") p("u") p("l") p("l") / ^_ _ _ _;

	u(0x200B) d1 u(0x200B) > p("e") p("i") p("n") p("s") / ^_ _ _;

	u(0x200B) d2 u(0x200B) > p("z") p("w") p("e") p("i") / ^_ _ _;
	u(0x200B) d3 u(0x200B) > p("d") p("r") p("e") p("i") / ^_ _ _;
	u(0x200B) d4 u(0x200B) > p("v") p("i") p("e") p("r") / ^_ _ _;
	u(0x200B) d5 u(0x200B) > p("f") u(0x00FC) p("n") p("f") / ^_ _ _;
	u(0x200B) d6 u(0x200B) > p("s") p("e") p("c") p("h") p("s") / ^_ _ _;
	u(0x200B) d7 u(0x200B) > p("s") p("i") p("e") p("b") p("e") p("n") / ^_ _ _;
	u(0x200B) d8 u(0x200B) > p("a") p("c") p("h") p("t") / ^_ _ _;
	u(0x200B) d9 u(0x200B) > p("n") p("e") p("u") p("n") / ^_ _ _;

	u(0x200B) d1 d0 u(0x200B) > p("z") p("e") p("h") p("n") / ^_ _ _ _;
	u(0x200B) d1 d1 u(0x200B) > p("e") p("l") p("f") / ^_ _ _ _;
	u(0x200B) d1 d2 u(0x200B) > p("z") p("w") u(0x00f6) p("l") p("f") / ^_ _ _ _;
	u(0x200B) d1 d6 u(0x200B) > p("s") p("e") p("c") p("h") p("z") p("e") p("h") p("n") / ^_ _ _ _;
	u(0x200B) d1 d7 u(0x200B) > p("s") p("i") p("e") p("b") p("z") p("e") p("h") p("n") / ^_ _ _ _;
	u(0x200B) d1 dd u(0x200B) > u(0x200B) @3 u(0x200B) p("z") p("e") p("h") p("n") / ^_ _ _ _;

	u(0x200B) d2 d0 u(0x200B) > p("z") p("w") p("a") p("n") p("z") p("i") p("g") / ^_ _ _ _;
	u(0x200B) d3 d0 u(0x200B) > p("d") p("r") p("e") p("i") u(0x00DF) p("i") p("g") / ^_ _ _ _;
	u(0x200B) d6 d0 u(0x200B) > p("s") p("e") p("c") p("h") p("z") p("i") p("g") / ^_ _ _ _;
	u(0x200B) d7 d0 u(0x200B) > p("s") p("i") p("e") p("b") p("z") p("i") p("g") / ^_ _ _ _;
	u(0x200B) dx d0 u(0x200B) > u(0x200B) @2 u(0x200B) p("z") p("i") p("g") / ^_ _ _ _;

	u(0x200B) dd dd u(0x200B) > u(0x200B) @3 u(0x200B) p("u") p("n") p("d") u(0x200B) @2 d0 u(0x200B) / ^_ _ _ _;

	u(0x200B) dx dd dd u(0x200B) > u(0x200B) @2 u(0x200B) p("h") p("u") p("n") p("d") p("e") p("r") p("t") u(0x200B) @3 @4 u(0x200B) / ^_ _ _ _ _;
	u(0x200B) dd dd dd dd u(0x200B) > u(0x200B) @2 u(0x200B) p("t") p("a") p("u") p("s") p("e") p("n") p("d") u(0x200B) @3 @4 @5 u(0x200B) / ^_ _ _ _ _;
	u(0x200B) dd dd dd dd dd u(0x200B) > u(0x200B) @2 @3 u(0x200B) p("t") p("a") p("u") p("s") p("e") p("n") p("d") u(0x200B) @4 @5 @6 u(0x200B) / ^_ _ _ _ _ _;
	u(0x200B) dd dd dd dd dd dd u(0x200B) > u(0x200B) @2 @3 @4 u(0x200B) p("t") p("a") p("u") p("s") p("e") p("n") p("d") u(0x200B) @5 @6 @7 u(0x200B) / ^_ _ _ _ _ _;

	u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("e") p("i") p("n") p("e")  u(0x0020) p("M") p("i") p("l") p("l") p("i") p("o") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
	u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("M") p("i") p("l") p("l") p("i") p("o") p("n") p("e") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
	u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("M") p("i") p("l") p("l") p("i") p("o") p("n") p("e") p("n")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
	u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("M") p("i") p("l") p("l") p("i") p("o") p("n") p("e") p("n")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;

endif;

	// boundary signs (first step to number handling)
	dd > u(0x200B) u(0x200B) @1 u(0x200B) u(0x200B) / ^_;
	dd dd  > u(0x200B) u(0x200B) @1 @2 u(0x200B) u(0x200B) / ^_ _;
	dd dd dd  > u(0x200B) u(0x200B) @1 @2 @3 u(0x200B) u(0x200B) / ^_ _ _;
	dd dd dd dd  > u(0x200B) u(0x200B) @1 @2 @3 @4 u(0x200B) u(0x200B) / ^_ _ _ _;
	dd dd dd dd dd  > u(0x200B) u(0x200B) @1 @2 @3 @4 @5 u(0x200B) u(0x200B) / ^_ _ _ _ _;
	dd dd dd dd dd dd  > u(0x200B) u(0x200B) @1 @2 @3 @4 @5 @6 u(0x200B) u(0x200B) / ^_ _ _ _ _ _;
	dd dd dd dd dd dd dd  > u(0x200B) u(0x200B) @1 @2 @3 @4 @5 @6 @7 u(0x200B) u(0x200B) / ^_ _ _ _ _ _ _;
	dd dd dd dd dd dd dd dd  > u(0x200B) u(0x200B) @1 @2 @3 @4 @5 @6 @7 @8 u(0x200B) u(0x200B) / ^_ _ _ _ _ _ _ _;
	dd dd dd dd dd dd dd dd dd  > u(0x200B) u(0x200B) @1 @2 @3 @4 @5 @6 @7 @8 @9 u(0x200B) u(0x200B) / ^_ _ _ _ _ _ _ _ _;
	dd dd dd dd dd dd dd dd dd dd > u(0x200B) u(0x200B) @1 @2 @3 @4 @5 @6 @7 @8 @9 @10 u(0x200B) u(0x200B) / ^_ _ _ _ _ _ _ _ _ _;
	dd dd dd dd dd dd dd dd dd dd dd > u(0x200B) u(0x200B) @1 @2 @3 @4 @5 @6 @7 @8 @9 @10 @11 u(0x200B) u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _;
	dd dd dd dd dd dd dd dd dd dd dd dd > u(0x200B) u(0x200B) @1 @2 @3 @4 @5 @6 @7 @8 @9 @10 @11 @12 u(0x200B) u(0x200B) / ^_ _ _ _ _ _ _ _ _ _ _ _;
endif;
	

if (numt == 1 && lng == AFK)

u(0x200B) u(0x200B) d0 u(0x200B) u(0x200B) > p("n") p("u") p("l") / ^_  _  _  _  _  ;
u(0x200B) d1  u(0x200B) > p("e") p("e") p("n") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("t") p("w") p("e") p("e") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("d") p("r") p("i") p("e") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("v") p("i") p("e") p("r") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("v") p("y") p("f") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("e") p("s") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("w") p("e") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("a") p("g") p("t") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("e") p("g") p("e") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("e") p("l") p("f") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("t") p("w") p("a") p("a") p("l") p("f") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("d") p("e") p("r") p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("v") p("e") p("e") p("r") p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d7  u(0x200B) > p("s") p("e") p("w") p("e") p("n") p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) > p("n") p("e") p("g") p("e") p("n") p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)   u(0x200B) p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("t") p("w") p("i") p("n") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d3 d0  u(0x200B) > p("d") p("e") p("r") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d4 d0  u(0x200B) > p("v") p("e") p("e") p("r") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d7 d0  u(0x200B) > p("s") p("e") p("w") p("e") p("n") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d8 d0  u(0x200B) > p("t") p("a") p("g") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d9 d0  u(0x200B) > p("n") p("e") p("g") p("e") p("n") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) dx d0  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @3 u(0x200B)   u(0x002D) p("e") p("n")  u(0x002D) u(0x200B)  @2  d0 u(0x200B) / ^_  _  _   _  ;
endif;
if (numt == 1 && lng == CAT)

u(0x200B) u(0x200B) d0  u(0x200B) > p("z") p("e") p("r") p("o") / ^_  _  _   _  ;
u(0x200B) d1 u(0x200B) u(0x200B) > p("u") / ^_  _  _  _  ;
u(0x200B) d1  u(0x200B) > p("u") p("n") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("d") p("o") p("s") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("e") p("s") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("q") p("u") p("a") p("t") p("r") p("e") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("c") p("i") p("n") p("c") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("i") p("s") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("t") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("v") p("u") p("i") p("t") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("o") p("u") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("e") p("u") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("o") p("n") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("d") p("o") p("t") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("t") p("r") p("e") p("t") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("c") p("a") p("t") p("o") p("r") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("q") p("u") p("i") p("n") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("s") p("e") p("t") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d7  u(0x200B) > p("d") p("i") p("s") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) > p("d") p("i")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("v") p("i") p("n") p("t") / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) > p("v") p("i") p("n") p("t")  u(0x002D) p("i")  u(0x002D)  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d3 d0  u(0x200B) > p("t") p("r") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d4 d0  u(0x200B) > p("q") p("u") p("a") p("r") p("a") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d5 d0  u(0x200B) > p("c") p("i") p("n") p("q") p("u") p("a") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d6 d0  u(0x200B) > p("s") p("e") p("i") p("x") p("a") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d7 d0  u(0x200B) > p("s") p("e") p("t") p("a") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d8 d0  u(0x200B) > p("v") p("u") p("i") p("t") p("a") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d9 d0  u(0x200B) > p("n") p("o") p("r") p("a") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) > u(0x200B)  @2  d0 u(0x200B)  u(0x002D)  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("c") p("e") p("n") p("t")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x002D) p("c") p("e") p("n") p("t") p("s")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("m") p("i") p("l")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("u") p("n")  u(0x0020) p("m") p("i") p("l") p("i")  u(0x00F3)  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("s")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("s")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("s")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == CSY)

u(0x200B) u(0x200B) d0  u(0x200B) > p("n") p("u") p("l") p("a") / ^_  _  _   _  ;
u(0x200B) u(0x200B) d1 u(0x200B) u(0x200B) > p("j") p("e") p("d") p("n") p("o") / ^_  _  _  _  _  ;
u(0x200B) d1  u(0x200B) > p("j") p("e") p("d") p("e") p("n") / ^_  _   _  ;
u(0x200B) u(0x200B) d2 u(0x200B) u(0x200B) > p("d") p("v")  u(0x011B) / ^_  _  _  _  _  ;
u(0x200B) d2  u(0x200B) > p("d") p("v") p("a") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t")  u(0x0159) p("i") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) >  u(0x010D) p("t") p("y")  u(0x0159) p("i") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("p")  u(0x011B) p("t") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) >  u(0x0161) p("e") p("s") p("t") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("d") p("m") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("s") p("m") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("d") p("e") p("v")  u(0x011B) p("t") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("e") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("j") p("e") p("d") p("e") p("n")  u(0x00E1) p("c") p("t") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) >  u(0x010D) p("t") p("r") p("n")  u(0x00E1) p("c") p("t") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("p") p("a") p("t") p("n")  u(0x00E1) p("c") p("t") / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) > p("d") p("e") p("v") p("a") p("t") p("e") p("n")  u(0x00E1) p("c") p("t") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("n")  u(0x00E1) p("c") p("t") / ^_  _  _   _  ;
u(0x200B) (d2,d3,d4) dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("c") p("e") p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d5 dd  u(0x200B) > p("p") p("a") p("d") p("e") p("s")  u(0x00E1) p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d6 dd  u(0x200B) >  u(0x0161) p("e") p("d") p("e") p("s")  u(0x00E1) p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) > p("d") p("e") p("v") p("a") p("d") p("e") p("s")  u(0x00E1) p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("d") p("e") p("s")  u(0x00E1) p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("s") p("t") p("o")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d2 dd  dd  u(0x200B) > p("d") p("v")  u(0x011B)  u(0x0020) p("s") p("t")  u(0x011B)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) (d3,d4) dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("s") p("t") p("a")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("s") p("e") p("t")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd  dd  dd  u(0x200B) > p("t") p("i") p("s")  u(0x00ED) p("c")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) (d2,d3,d4) dd  dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("t") p("i") p("s")  u(0x00ED) p("c") p("e")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) dx dd  dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("t") p("i") p("s")  u(0x00ED) p("c") p("e")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) dx dd dd  dd  dd  u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("t") p("i") p("s")  u(0x00ED) p("c") p("e")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _   _   _   _  ;
u(0x200B) dx dd dd dd  dd  dd  u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("t") p("i") p("s")  u(0x00ED) p("c") p("e")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _   _   _   _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("m") p("i") p("l") p("i") p("o") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) (d2,d3,d4) dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("y")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n")  u(0x016F)  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n")  u(0x016F)  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n")  u(0x016F)  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == DAN)

u(0x200B) u(0x200B) d0  u(0x200B) > p("n") p("u") p("l") / ^_  _  _   _  ;
u(0x200B) d1 u(0x200B) u(0x200B) > p("e") p("n") / ^_  _  _  _  ;
u(0x200B) d1  u(0x200B) > p("e") p("t") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("t") p("o") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("e") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("f") p("i") p("r") p("e") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("f") p("e") p("m") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("e") p("k") p("s") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("y") p("v") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("t") p("t") p("e") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("i") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("t") p("i") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("e") p("l") p("l") p("e") p("v") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("t") p("o") p("l") p("v") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("t") p("r") p("e") p("t") p("t") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("f") p("j") p("o") p("r") p("t") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("f") p("e") p("m") p("t") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("s") p("e") p("k") p("s") p("t") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d7  u(0x200B) > p("s") p("y") p("t") p("t") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d8  u(0x200B) > p("a") p("t") p("t") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) > p("n") p("i") p("t") p("t") p("e") p("n")  u(0x0020) / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("t") p("y") p("v") p("e") / ^_  _  _   _  ;
u(0x200B) d3 d0  u(0x200B) > p("t") p("r") p("e") p("d") p("i") p("v") p("e") / ^_  _  _   _  ;
u(0x200B) d4 d0  u(0x200B) > p("f") p("y") p("r") p("r") p("e") / ^_  _  _   _  ;
u(0x200B) d5 d0  u(0x200B) > p("h") p("a") p("l") p("v") p("t") p("r") p("e") p("d") p("s") / ^_  _  _   _  ;
u(0x200B) d6 d0  u(0x200B) > p("t") p("r") p("e") p("s") / ^_  _  _   _  ;
u(0x200B) d7 d0  u(0x200B) > p("h") p("a") p("l") p("v") p("f") p("j") p("e") p("r") p("d") p("s") / ^_  _  _   _  ;
u(0x200B) d8 d0  u(0x200B) > p("f") p("i") p("r") p("s") / ^_  _  _   _  ;
u(0x200B) d9 d0  u(0x200B) > p("h") p("a") p("l") p("v") p("f") p("e") p("m") p("s") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @3 u(0x200B)   u(0x200B) p("o") p("g") u(0x200B)  @2  d0 u(0x200B) / ^_  _  _   _  ;
endif;
if (numt == 1 && lng == ELL)

u(0x200B) u(0x200B) d0  u(0x200B) >  u(0x03BC)  u(0x03B7)  u(0x03B4)  u(0x03AD)  u(0x03BD) / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) >  u(0x03AD)  u(0x03BD)  u(0x03B1) / ^_  _   _  ;
u(0x200B) d2  u(0x200B) >  u(0x03B4)  u(0x03CD)  u(0x03BF) / ^_  _   _  ;
u(0x200B) d3 u(0x200B) u(0x200B) >  u(0x03C4)  u(0x03C1)  u(0x03AF)  u(0x03B1) / ^_  _  _  _  ;
u(0x200B) d3  u(0x200B) >  u(0x03C4)  u(0x03C1)  u(0x03B5)  u(0x03B9)  u(0x03C2) / ^_  _   _  ;
u(0x200B) d4 u(0x200B) u(0x200B) >  u(0x03C4)  u(0x03AD)  u(0x03C3)  u(0x03C3)  u(0x03B5)  u(0x03C1)  u(0x03B1) / ^_  _  _  _  ;
u(0x200B) d4  u(0x200B) >  u(0x03C4)  u(0x03AD)  u(0x03C3)  u(0x03C3)  u(0x03B5)  u(0x03C1)  u(0x03B9)  u(0x03C2) / ^_  _   _  ;
u(0x200B) d5  u(0x200B) >  u(0x03C0)  u(0x03AD)  u(0x03BD)  u(0x03C4)  u(0x03B5) / ^_  _   _  ;
u(0x200B) d6  u(0x200B) >  u(0x03AD)  u(0x03BE)  u(0x03B9) / ^_  _   _  ;
u(0x200B) d7  u(0x200B) >  u(0x03B5)  u(0x03C0)  u(0x03C4)  u(0x03AC) / ^_  _   _  ;
u(0x200B) d8  u(0x200B) >  u(0x03BF)  u(0x03BA)  u(0x03C4)  u(0x03CE) / ^_  _   _  ;
u(0x200B) d9  u(0x200B) >  u(0x03B5)  u(0x03BD)  u(0x03BD)  u(0x03AD)  u(0x03B1) / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) >  u(0x03B4)  u(0x03AD)  u(0x03BA)  u(0x03B1) / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) >  u(0x03AD)  u(0x03BD)  u(0x03C4)  u(0x03B5)  u(0x03BA)  u(0x03B1) / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) >  u(0x03B4)  u(0x03CE)  u(0x03B4)  u(0x03B5)  u(0x03BA)  u(0x03B1) / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x03B4)  u(0x03B5)  u(0x03BA)  u(0x03B1)  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) >  u(0x03B5)  u(0x03AF)  u(0x03BA)  u(0x03BF)  u(0x03C3)  u(0x03B9)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d3 dd  u(0x200B) >  u(0x03C4)  u(0x03C1)  u(0x03B9)  u(0x03AC)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) >  u(0x03C3)  u(0x03B1)  u(0x03C1)  u(0x03AC)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d5 dd  u(0x200B) >  u(0x03C0)  u(0x03B5)  u(0x03BD)  u(0x03AE)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d6 dd  u(0x200B) >  u(0x03B5)  u(0x03BE)  u(0x03AE)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d7 dd  u(0x200B) >  u(0x03B5)  u(0x03B2)  u(0x03B4)  u(0x03BF)  u(0x03BC)  u(0x03AE)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d8 dd  u(0x200B) >  u(0x03BF)  u(0x03B3)  u(0x03B4)  u(0x03CC)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) >  u(0x03B5)  u(0x03BD)  u(0x03B5)  u(0x03BD)  u(0x03AE)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 d0 d0  u(0x200B) >  u(0x03B5)  u(0x03BA)  u(0x03B1)  u(0x03C4)  u(0x03CC) / ^_  _  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) >  u(0x03B5)  u(0x03BA)  u(0x03B1)  u(0x03C4)  u(0x03CC)  u(0x03BD)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d2 dd  dd u(0x200B) u(0x200B) >  u(0x03B4)  u(0x03B9)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _  _  _  ;
u(0x200B) d2 dd  dd  u(0x200B) >  u(0x03B4)  u(0x03B9)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d3 dd  dd u(0x200B) u(0x200B) >  u(0x03C4)  u(0x03C1)  u(0x03B9)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _  _  _  ;
u(0x200B) d3 dd  dd  u(0x200B) >  u(0x03C4)  u(0x03C1)  u(0x03B9)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d4 dd  dd u(0x200B) u(0x200B) >  u(0x03C4)  u(0x03B5)  u(0x03C4)  u(0x03C1)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _  _  _  ;
u(0x200B) d4 dd  dd  u(0x200B) >  u(0x03C4)  u(0x03B5)  u(0x03C4)  u(0x03C1)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d5 dd  dd u(0x200B) u(0x200B) >  u(0x03C0)  u(0x03B5)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _  _  _  ;
u(0x200B) d5 dd  dd  u(0x200B) >  u(0x03C0)  u(0x03B5)  u(0x03BD)  u(0x03C4)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d6 dd  dd u(0x200B) u(0x200B) >  u(0x03B5)  u(0x03BE)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _  _  _  ;
u(0x200B) d6 dd  dd  u(0x200B) >  u(0x03B5)  u(0x03BE)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d7 dd  dd u(0x200B) u(0x200B) >  u(0x03B5)  u(0x03C0)  u(0x03C4)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _  _  _  ;
u(0x200B) d7 dd  dd  u(0x200B) >  u(0x03B5)  u(0x03C0)  u(0x03C4)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d8 dd  dd u(0x200B) u(0x200B) >  u(0x03BF)  u(0x03BA)  u(0x03C4)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _  _  _  ;
u(0x200B) d8 dd  dd  u(0x200B) >  u(0x03BF)  u(0x03BA)  u(0x03C4)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d9 dd  dd u(0x200B) u(0x200B) >  u(0x03B5)  u(0x03BD)  u(0x03BD)  u(0x03B9)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _  _  _  ;
u(0x200B) d9 dd  dd  u(0x200B) >  u(0x03B5)  u(0x03BD)  u(0x03BD)  u(0x03B9)  u(0x03B1)  u(0x03BA)  u(0x03CC)  u(0x03C3)  u(0x03B9)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) >  u(0x03C7)  u(0x03AF)  u(0x03BB)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020)  u(0x03C7)  u(0x03B9)  u(0x03BB)  u(0x03B9)  u(0x03AC)  u(0x03B4)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020)  u(0x03C7)  u(0x03B9)  u(0x03BB)  u(0x03B9)  u(0x03AC)  u(0x03B4)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020)  u(0x03C7)  u(0x03B9)  u(0x03BB)  u(0x03B9)  u(0x03AC)  u(0x03B4)  u(0x03B5)  u(0x03C2)  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) >  u(0x03AD)  u(0x03BD)  u(0x03B1)  u(0x0020)  u(0x03B5)  u(0x03BA)  u(0x03B1)  u(0x03C4)  u(0x03BF)  u(0x03BC)  u(0x03BC)  u(0x03CD)  u(0x03C1)  u(0x03B9)  u(0x03BF)  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B)  u(0x0020)  u(0x03B5)  u(0x03BA)  u(0x03B1)  u(0x03C4)  u(0x03BF)  u(0x03BC)  u(0x03BC)  u(0x03CD)  u(0x03C1)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x200B)  u(0x0020)  u(0x03B5)  u(0x03BA)  u(0x03B1)  u(0x03C4)  u(0x03BF)  u(0x03BC)  u(0x03BC)  u(0x03CD)  u(0x03C1)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x200B)  u(0x0020)  u(0x03B5)  u(0x03BA)  u(0x03B1)  u(0x03C4)  u(0x03BF)  u(0x03BC)  u(0x03BC)  u(0x03CD)  u(0x03C1)  u(0x03B9)  u(0x03B1)  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == EO)

u(0x200B) u(0x200B) d0  u(0x200B) > p("n") p("u") p("l") p("o") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("u") p("n") p("u") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("d") p("u") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("i") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("k") p("v") p("a") p("r") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("k") p("v") p("i") p("n") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("e") p("s") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("p") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("k") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("a")  u(0x016D) / ^_  _   _  ;
u(0x200B) d1 dd  u(0x200B) > p("d") p("e") p("k")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("d") p("e") p("k")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("c") p("e") p("n") p("t")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("c") p("e") p("n") p("t")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("m") p("i") p("l")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("u") p("n") p("u")  u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("o")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("o") p("j")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("o") p("j")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("o") p("j")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == ESP)

u(0x200B) u(0x200B) d0  u(0x200B) > p("c") p("e") p("r") p("o") / ^_  _  _   _  ;
u(0x200B) d1 u(0x200B) u(0x200B) > p("u") p("n") p("o") / ^_  _  _  _  ;
u(0x200B) d1  u(0x200B) > p("u") p("n") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("d") p("o") p("s") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("e") p("s") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("c") p("u") p("a") p("t") p("r") p("o") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("c") p("i") p("n") p("c") p("o") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("e") p("i") p("s") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("i") p("e") p("t") p("e") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("c") p("h") p("o") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("u") p("e") p("v") p("e") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("i") p("e") p("z") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("o") p("n") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("d") p("o") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("t") p("r") p("e") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("c") p("a") p("t") p("o") p("r") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("q") p("u") p("i") p("n") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("d") p("i") p("e") p("c") p("i") p("s")  u(0x00E9) p("i") p("s") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) > p("d") p("i") p("e") p("c") p("i")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("v") p("e") p("i") p("n") p("t") p("e") / ^_  _  _   _  ;
u(0x200B) d2 d2  u(0x200B) > p("v") p("e") p("i") p("n") p("t") p("i") p("d")  u(0x00F3) p("s") / ^_  _  _   _  ;
u(0x200B) d2 d3  u(0x200B) > p("v") p("e") p("i") p("n") p("t") p("i") p("t") p("r")  u(0x00E9) p("s") / ^_  _  _   _  ;
u(0x200B) d2 d6  u(0x200B) > p("v") p("e") p("i") p("n") p("t") p("i") p("s")  u(0x00E9) p("i") p("s") / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) > p("v") p("e") p("i") p("n") p("t") p("i")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d3 d0  u(0x200B) > p("t") p("r") p("e") p("i") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d4 d0  u(0x200B) > p("c") p("u") p("a") p("r") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d5 d0  u(0x200B) > p("c") p("i") p("n") p("c") p("u") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d6 d0  u(0x200B) > p("s") p("e") p("s") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d7 d0  u(0x200B) > p("s") p("e") p("t") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d8 d0  u(0x200B) > p("o") p("c") p("h") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d9 d0  u(0x200B) > p("n") p("o") p("v") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) > u(0x200B)  @2  d0 u(0x200B)  u(0x0020) p("y")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 d0 d0  u(0x200B) > p("c") p("i") p("e") p("n") / ^_  _  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("c") p("i") p("e") p("n") p("t") p("o")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d5 dd  dd  u(0x200B) > p("q") p("u") p("i") p("n") p("i") p("e") p("n") p("t") p("o") p("s")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d7 dd  dd  u(0x200B) > p("s") p("e") p("t") p("e") p("c") p("i") p("e") p("n") p("t") p("o") p("s")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d9 dd  dd  u(0x200B) > p("n") p("o") p("v") p("e") p("c") p("i") p("e") p("n") p("t") p("o") p("s")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("c") p("i") p("e") p("n") p("t") p("o") p("s")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("m") p("i") p("l")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("u") p("n")  u(0x0020) p("m") p("i") p("l") p("l")  u(0x00F3) p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("o") p("n") p("e") p("s")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("o") p("n") p("e") p("s")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("o") p("n") p("e") p("s")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == FIN)

u(0x200B) u(0x200B) d0  u(0x200B) > p("n") p("o") p("l") p("l") p("a") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("y") p("k") p("s") p("i") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("k") p("a") p("k") p("s") p("i") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("k") p("o") p("l") p("m") p("e") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("n") p("e") p("l") p("j")  u(0x00E4) / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("v") p("i") p("i") p("s") p("i") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("k") p("u") p("u") p("s") p("i") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("i") p("t") p("s") p("e") p("m")  u(0x00E4) p("n") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("k") p("a") p("h") p("d") p("e") p("k") p("s") p("a") p("n") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("y") p("h") p("d") p("e") p("k") p("s")  u(0x00E4) p("n") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("k") p("y") p("m") p("m") p("e") p("n") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("t") p("o") p("i") p("s") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("k") p("y") p("m") p("m") p("e") p("n") p("t")  u(0x00E4)  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("s") p("a") p("t") p("a")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("s") p("a") p("t") p("a") p("a")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("t") p("u") p("h") p("a") p("t")  u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)  p("t") p("u") p("h") p("a") p("t") p("t") p("a")  u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)  p("t") p("u") p("h") p("a") p("t") p("t") p("a")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)  p("t") p("u") p("h") p("a") p("t") p("t") p("a")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("m") p("i") p("l") p("j") p("o") p("o") p("n") p("a")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("j") p("o") p("o") p("n") p("a") p("a")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("j") p("o") p("o") p("n") p("a") p("a")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("j") p("o") p("o") p("n") p("a") p("a")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == FRA)

u(0x200B) u(0x200B) d0  u(0x200B) > p("z")  u(0x00E9) p("r") p("o") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("u") p("n") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("d") p("e") p("u") p("x") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("o") p("i") p("s") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("q") p("u") p("a") p("t") p("r") p("e") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("c") p("i") p("n") p("q") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("i") p("x") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("p") p("t") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("h") p("u") p("i") p("t") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("e") p("u") p("f") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("i") p("x") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("o") p("n") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("d") p("o") p("u") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("t") p("r") p("e") p("i") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("q") p("u") p("a") p("t") p("o") p("r") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("q") p("u") p("i") p("n") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("s") p("e") p("i") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("v") p("i") p("n") p("g") p("t") / ^_  _  _   _  ;
u(0x200B) d3 d0  u(0x200B) > p("t") p("r") p("e") p("n") p("t") p("e") / ^_  _  _   _  ;
u(0x200B) d4 d0  u(0x200B) > p("q") p("u") p("a") p("r") p("a") p("n") p("t") p("e") / ^_  _  _   _  ;
u(0x200B) d5 d0  u(0x200B) > p("c") p("i") p("n") p("q") p("u") p("a") p("n") p("t") p("e") / ^_  _  _   _  ;
u(0x200B) d6 d0  u(0x200B) > p("s") p("o") p("i") p("x") p("a") p("n") p("t") p("e") / ^_  _  _   _  ;
u(0x200B) d7 d1  u(0x200B) > p("s") p("o") p("i") p("x") p("a") p("n") p("t") p("e")  u(0x0020) p("e") p("t")  u(0x0020) p("o") p("n") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d7 dd  u(0x200B) > p("s") p("o") p("i") p("x") p("a") p("n") p("t") p("e")  u(0x002D) u(0x200B) d1  @3  u(0x200B) / ^_  _  _   _  ;
u(0x200B) d8 d0 u(0x200B) u(0x200B) > p("q") p("u") p("a") p("t") p("r") p("e")  u(0x002D) p("v") p("i") p("n") p("g") p("t") p("s") / ^_  _  _  _  _  ;
u(0x200B) d8 d0  u(0x200B) > p("q") p("u") p("a") p("t") p("r") p("e")  u(0x002D) p("v") p("i") p("n") p("g") p("t") / ^_  _  _   _  ;
u(0x200B) d8 d1  u(0x200B) > p("q") p("u") p("a") p("t") p("r") p("e")  u(0x002D) p("v") p("i") p("n") p("g") p("t")  u(0x002D) p("u") p("n") / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) > p("q") p("u") p("a") p("t") p("r") p("e")  u(0x002D) p("v") p("i") p("n") p("g") p("t")  u(0x002D) u(0x200B) d1  @3  u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx d1  u(0x200B) > u(0x200B)  @2  d0 u(0x200B)  u(0x0020) p("e") p("t")  u(0x0020) p("u") p("n") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) > u(0x200B)  @2  d0 u(0x200B)  u(0x002D)  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("c") p("e") p("n") p("t")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) (d2,d3,d4,d5,d6,d7,d8,d9) d0 d0 u(0x200B) u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("c") p("e") p("n") p("t") p("s") / ^_  _  _  _  _  _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("c") p("e") p("n") p("t")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 d1 d0 d0  u(0x200B) > p("o") p("n") p("z") p("e")  u(0x0020) p("c") p("e") p("n") p("t") p("s") / ^_  _  _  _  _   _  ;
u(0x200B) d1 d1 dd  dd  u(0x200B) > p("o") p("n") p("z") p("e")  u(0x0020) p("c") p("e") p("n") p("t")  u(0x003A) u(0x003A) @4 @5 u(0x200B) @4 @5 u(0x200B) / ^_  _  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("m") p("i") p("l") p("l") p("e")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("e")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("e")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("l") p("e")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("u") p("n")  u(0x0020) p("m") p("i") p("l") p("l") p("i") p("o") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B)  u(0x0020) p("m") p("i") p("l") p("l") p("i") p("o") p("n") p("s")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x200B)  u(0x0020) p("m") p("i") p("l") p("l") p("i") p("o") p("n") p("s")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x200B)  u(0x0020) p("m") p("i") p("l") p("l") p("i") p("o") p("n") p("s")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == ITA)

u(0x200B) u(0x200B) d0  u(0x200B) > p("z") p("e") p("r") p("o") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("u") p("n") p("o") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("d") p("u") p("e") / ^_  _   _  ;
u(0x200B) u(0x200B) d3 u(0x200B) u(0x200B) > p("t") p("r") p("e") / ^_  _  _  _  _  ;
u(0x200B) d3 u(0x200B) u(0x200B) > p("t") p("r")  u(0x00E9) / ^_  _  _  _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("e") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("q") p("u") p("a") p("t") p("t") p("r") p("o") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("c") p("i") p("n") p("q") p("u") p("e") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("e") p("i") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("t") p("t") p("e") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("t") p("t") p("o") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("o") p("v") p("e") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("i") p("e") p("c") p("i") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("u") p("n") p("d") p("i") p("c") p("i") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("d") p("o") p("d") p("i") p("c") p("i") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("t") p("r") p("e") p("d") p("i") p("c") p("i") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("q") p("u") p("a") p("t") p("t") p("o") p("r") p("d") p("i") p("c") p("i") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("q") p("u") p("i") p("n") p("d") p("i") p("c") p("i") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("s") p("e") p("d") p("i") p("c") p("i") / ^_  _  _   _  ;
u(0x200B) d1 d7  u(0x200B) > p("d") p("i") p("c") p("i") p("a") p("s") p("s") p("e") p("t") p("t") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d8  u(0x200B) > p("d") p("i") p("c") p("i") p("o") p("t") p("t") p("o") / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) > p("d") p("i") p("c") p("i") p("a") p("n") p("n") p("o") p("v") p("e") / ^_  _  _   _  ;
u(0x200B) d2 (d1,d8) u(0x200B) > p("v") p("e") p("n") p("t")  u(0x200B) @3 u(0x200B) / ^_  _  _  _  ;
u(0x200B) d2 dd  u(0x200B) > p("v") p("e") p("n") p("t") p("i")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d3 (d1,d8) u(0x200B) > p("t") p("r") p("e") p("n") p("t")  u(0x200B) @3 u(0x200B) / ^_  _  _  _  ;
u(0x200B) d3 dd  u(0x200B) > p("t") p("r") p("e") p("n") p("t") p("a")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d4 (d1,d8) u(0x200B) > p("q") p("u") p("a") p("r") p("a") p("n") p("t")  u(0x200B) @3 u(0x200B) / ^_  _  _  _  ;
u(0x200B) d4 dd  u(0x200B) > p("q") p("u") p("a") p("r") p("a") p("n") p("t") p("a")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d5 (d1,d8) u(0x200B) > p("c") p("i") p("n") p("q") p("u") p("a") p("n") p("t")  u(0x200B) @3 u(0x200B) / ^_  _  _  _  ;
u(0x200B) d5 dd  u(0x200B) > p("c") p("i") p("n") p("q") p("u") p("a") p("n") p("t") p("a")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d6 (d1,d8) u(0x200B) > p("s") p("e") p("s") p("s") p("a") p("n") p("t")  u(0x200B) @3 u(0x200B) / ^_  _  _  _  ;
u(0x200B) d6 dd  u(0x200B) > p("s") p("e") p("s") p("s") p("a") p("n") p("t") p("a")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d7 (d1,d8) u(0x200B) > p("s") p("e") p("t") p("t") p("a") p("n") p("t")  u(0x200B) @3 u(0x200B) / ^_  _  _  _  ;
u(0x200B) d7 dd  u(0x200B) > p("s") p("e") p("t") p("t") p("a") p("n") p("t") p("a")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d8 (d1,d8) u(0x200B) > p("o") p("t") p("t") p("a") p("n") p("t")  u(0x200B) @3 u(0x200B) / ^_  _  _  _  ;
u(0x200B) d8 dd  u(0x200B) > p("o") p("t") p("t") p("a") p("n") p("t") p("a")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d9 (d1,d8) u(0x200B) > p("n") p("o") p("v") p("a") p("n") p("t")  u(0x200B) @3 u(0x200B) / ^_  _  _  _  ;
u(0x200B) d9 dd  u(0x200B) > p("n") p("o") p("v") p("a") p("n") p("t") p("a")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("c") p("e") p("n") p("t") p("o")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("c") p("e") p("n") p("t") p("o")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("m") p("i") p("l") p("l") p("e")  u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)  p("m") p("i") p("l") p("a")  u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)  p("m") p("i") p("l") p("a")  u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)  p("m") p("i") p("l") p("a")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("u") p("n")  u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("e")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("i")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("i")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("o") p("n") p("i")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == LTZ)

u(0x200B) u(0x200B) d0  u(0x200B) > p("n") p("u") p("l") p("l") / ^_  _  _   _  ;
u(0x200B) d1 u(0x200B) u(0x200B) > p("e") p("e") p("n") p("t") / ^_  _  _  _  ;
u(0x200B) d1  u(0x200B) > p("e") p("e") p("n") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("z") p("w") p("e") p("e") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("d") p("r")  u(0x00E4) p("i") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("v")  u(0x00E9) p("i") p("e") p("r") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("f")  u(0x00EB) p("n") p("n") p("e") p("f") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("e") p("c") p("h") p("s") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("i") p("w") p("e") p("n") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("a") p("a") p("c") p("h") p("t") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n")  u(0x00E9) p("n") p("g") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("z")  u(0x00E9) p("n") p("g") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("e") p("e") p("l") p("e") p("f") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("z") p("w") p("i") p("e") p("l") p("e") p("f") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("f") p("o") p("f") p("z")  u(0x00E9) p("n") p("g") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("s") p("i") p("e") p("c") p("h") p("z")  u(0x00E9) p("n") p("g") / ^_  _  _   _  ;
u(0x200B) d1 d7  u(0x200B) > p("s") p("i") p("w") p("w") p("e") p("n") p("z")  u(0x00E9) p("n") p("g") / ^_  _  _   _  ;
u(0x200B) d1 d8  u(0x200B) > p("u") p("e") p("c") p("h") p("z")  u(0x00E9) p("n") p("g") / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) > p("n") p("o") p("n") p("z")  u(0x00E9) p("n") p("g") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("z")  u(0x00E9) p("n") p("g") / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("z") p("w") p("a") p("n") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("n") p("z") p("w") p("a") p("n") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d3 d0  u(0x200B) > p("d") p("r")  u(0x00EB) p("s") p("s") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d3 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("n") p("d") p("r")  u(0x00EB) p("s") p("s") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("v")  u(0x00E9) p("i") p("e") p("r") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d5 d0  u(0x200B) > p("f") p("o") p("f") p("f") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d5 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("f") p("o") p("f") p("f") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d6 d0  u(0x200B) > p("s") p("i") p("e") p("c") p("h") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d6 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("s") p("i") p("e") p("c") p("h") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d7 d0  u(0x200B) > p("s") p("i") p("w") p("w") p("e") p("n") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d7 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("s") p("i") p("w") p("w") p("e") p("n") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d8 d0  u(0x200B) > p("a") p("c") p("h") p("t") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d8 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("n") p("a") p("c") p("h") p("t") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d9 d0  u(0x200B) > p("n") p("o") p("n") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("n") p("n") p("o") p("n") p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) dx d0  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("a") p("n")  u(0x200B) @2 u(0x200B)  p("z") p("e") p("g") / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("h") p("o") p("n") p("n") p("e") p("r") p("t")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("h") p("o") p("n") p("n") p("e") p("r") p("t")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("d") p("a") p("u") p("s") p("e") p("n") p("d")  u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)  p("d") p("a") p("u") p("s") p("e") p("n") p("d")  u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)  p("d") p("a") p("u") p("s") p("e") p("n") p("d")  u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)  p("d") p("a") p("u") p("s") p("e") p("n") p("d")  u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("e") p("n") p("g")  u(0x0020) p("M") p("i") p("l") p("l") p("i") p("o") p("u") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("M") p("i") p("l") p("l") p("i") p("o") p("u") p("n") p("e") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("M") p("i") p("l") p("l") p("i") p("o") p("u") p("n") p("e") p("n")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("M") p("i") p("l") p("l") p("i") p("o") p("u") p("n") p("e") p("n")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == NLD)

u(0x200B) u(0x200B) d0 u(0x200B) u(0x200B) > p("n") p("u") p("l") / ^_  _  _  _  _  ;
u(0x200B) d1 u(0x200B) u(0x200B) > p("e") p("e") p("n") / ^_  _  _  _  ;
u(0x200B) d1  u(0x200B) > p("e") p("e") p("n") p("e") p("n") / ^_  _   _  ;
u(0x200B) d2 u(0x200B) u(0x200B) > p("t") p("w") p("e") p("e") / ^_  _  _  _  ;
u(0x200B) d2  u(0x200B) > p("t") p("w") p("e") p("e")  u(0x00EB) p("n") / ^_  _   _  ;
u(0x200B) d3 u(0x200B) u(0x200B) > p("d") p("r") p("i") p("e") / ^_  _  _  _  ;
u(0x200B) d3  u(0x200B) > p("d") p("r") p("i") p("e")  u(0x00EB) p("n") / ^_  _   _  ;
u(0x200B) d4 u(0x200B) u(0x200B) > p("v") p("i") p("e") p("r") / ^_  _  _  _  ;
u(0x200B) d4  u(0x200B) > p("v") p("i") p("e") p("r") p("e") p("n") / ^_  _   _  ;
u(0x200B) d5 u(0x200B) u(0x200B) > p("v") p("i") p("j") p("f") / ^_  _  _  _  ;
u(0x200B) d5  u(0x200B) > p("v") p("i") p("j") p("f") p("e") p("n") / ^_  _   _  ;
u(0x200B) d6 u(0x200B) u(0x200B) > p("z") p("e") p("s") / ^_  _  _  _  ;
u(0x200B) d6  u(0x200B) > p("z") p("e") p("s") p("e") p("n") / ^_  _   _  ;
u(0x200B) d7 u(0x200B) u(0x200B) > p("z") p("e") p("v") p("e") p("n") / ^_  _  _  _  ;
u(0x200B) d7  u(0x200B) > p("z") p("e") p("v") p("e") p("n") p("e") p("n") / ^_  _   _  ;
u(0x200B) d8 u(0x200B) u(0x200B) > p("a") p("c") p("h") p("t") / ^_  _  _  _  ;
u(0x200B) d8  u(0x200B) > p("a") p("c") p("h") p("t") p("e") p("n") / ^_  _   _  ;
u(0x200B) d9 u(0x200B) u(0x200B) > p("n") p("e") p("g") p("e") p("n") / ^_  _  _  _  ;
u(0x200B) d9  u(0x200B) > p("n") p("e") p("g") p("e") p("n") p("e") p("n") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("e") p("l") p("f") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("t") p("w") p("a") p("a") p("l") p("f") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("d") p("e") p("r") p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("v") p("e") p("e") p("r") p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)   u(0x200B) p("t") p("i") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("t") p("w") p("i") p("n") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d3 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("d") p("e") p("r") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("v") p("e") p("e") p("r") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d8 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("t") p("a") p("c") p("h") p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @3 u(0x200B)   SEPARATOR  u(0x200B) @2 u(0x200B)   u(0x200B) p("t") p("i") p("g") / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("h") p("o") p("n") p("d") p("e") p("r") p("d")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B) p("h") p("o") p("n") p("d") p("e") p("r") p("d")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 d0 dd dd u(0x200B) > p("d") p("u") p("i") p("z") p("e") p("n") p("d")  u(0x003A) u(0x003A) @4 @5 u(0x200B) @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx d0 dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B) p("d") p("u") p("i") p("z") p("e") p("n") p("d")  u(0x003A) u(0x003A) @4 @5 u(0x200B) @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) d1  dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x200B) p("h") p("o") p("n") p("d") p("e") p("r") p("d")  u(0x200B) @4 @5 u(0x200B) / ^_  _   _  _  _  _  ;
u(0x200B) dx  dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x200B) p("h") p("o") p("n") p("d") p("e") p("r") p("d")  u(0x200B) @4 @5 u(0x200B) / ^_  _   _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x200B) p("d") p("u") p("i") p("z") p("e") p("n") p("d")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x200B) p("d") p("u") p("i") p("z") p("e") p("n") p("d")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B)  u(0x0020) p("m") p("i") p("l") p("j") p("o") p("e") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x200B)  u(0x0020) p("m") p("i") p("l") p("j") p("o") p("e") p("n")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x200B)  u(0x0020) p("m") p("i") p("l") p("j") p("o") p("e") p("n")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == PLK)

u(0x200B) u(0x200B) d0  u(0x200B) > p("z") p("e") p("r") p("o") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("j") p("e") p("d") p("e") p("n") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("d") p("w") p("a") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("z") p("y") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("c") p("z") p("t") p("e") p("r") p("y") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("p") p("i")  u(0x0119)  u(0x0107) / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("z") p("e")  u(0x015B)  u(0x0107) / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("i") p("e") p("d") p("e") p("m") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("s") p("i") p("e") p("m") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("d") p("z") p("i") p("e") p("w") p("i")  u(0x0119)  u(0x0107) / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("z") p("i") p("e") p("s") p("i")  u(0x0119)  u(0x0107) / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("j") p("e") p("d") p("e") p("n") p("a")  u(0x015B) p("c") p("i") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("c") p("z") p("t") p("e") p("r") p("n") p("a")  u(0x015B) p("c") p("i") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("p") p("i")  u(0x0119) p("t") p("n") p("a")  u(0x015B) p("c") p("i") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("s") p("z") p("e") p("s") p("n") p("a")  u(0x015B) p("c") p("i") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) > p("d") p("z") p("i") p("e") p("w") p("i")  u(0x0119) p("t") p("n") p("a")  u(0x015B) p("c") p("i") p("e") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("n") p("a")  u(0x015B) p("c") p("i") p("e") / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) > p("d") p("w") p("a") p("d") p("z") p("i") p("e")  u(0x015B) p("c") p("i") p("a")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d3 dd  u(0x200B) > p("t") p("r") p("z") p("y") p("d") p("z") p("i") p("e")  u(0x015B) p("c") p("i")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) > p("c") p("z") p("t") p("e") p("r") p("d") p("z") p("i") p("e")  u(0x015B) p("c") p("i")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("d") p("z") p("i") p("e") p("s") p("i")  u(0x0105) p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("s") p("t") p("o")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d2 dd  dd  u(0x200B) > p("d") p("w") p("i") p("e")  u(0x015B) p("c") p("i") p("e")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) (d3,d4) dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("s") p("t") p("a")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("s") p("e") p("t")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("t") p("y") p("s") p("i")  u(0x0105) p("c")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) (d2,d3,d4) dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("t") p("y") p("s") p("i")  u(0x0105) p("c") p("e")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) (d2,d3,d4,d5,d6,d7,d8,d9) (d2,d3,d4) dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("t") p("y") p("s") p("i")  u(0x0105) p("c") p("e")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dd (d0,d2,d3,d4,d5,d6,d7,d8,d9) (d2,d3,d4) dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("t") p("y") p("s") p("i")  u(0x0105) p("c") p("e")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("t") p("y") p("s") p("i")  u(0x0119) p("c") p("y")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("t") p("y") p("s") p("i")  u(0x0119) p("c") p("y")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("t") p("y") p("s") p("i")  u(0x0119) p("c") p("y")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == PTG)

u(0x200B) u(0x200B) d0  u(0x200B) > p("z") p("e") p("r") p("o") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("u") p("m") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("d") p("o") p("i") p("s") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r")  u(0x00EA) p("s") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("q") p("u") p("a") p("t") p("r") p("o") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("c") p("i") p("n") p("c") p("o") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("e") p("i") p("s") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("t") p("e") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("i") p("t") p("o") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("o") p("v") p("e") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("e") p("z") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("o") p("n") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("d") p("o") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("t") p("r") p("e") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("q") p("u") p("a") p("t") p("o") p("r") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("q") p("u") p("i") p("n") p("z") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("d") p("e") p("z") p("a") p("s") p("s") p("e") p("i") p("s") / ^_  _  _   _  ;
u(0x200B) d1 d7  u(0x200B) > p("d") p("e") p("z") p("a") p("s") p("s") p("e") p("t") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d8  u(0x200B) > p("d") p("e") p("z") p("o") p("i") p("t") p("o") / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) > p("d") p("e") p("z") p("a") p("n") p("o") p("v") p("e") / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("v") p("i") p("n") p("t") p("e") / ^_  _  _   _  ;
u(0x200B) d3 d0  u(0x200B) > p("t") p("r") p("i") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d4 d0  u(0x200B) > p("q") p("u") p("a") p("r") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d5 d0  u(0x200B) > p("c") p("i") p("n") p("q") p("u") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d6 d0  u(0x200B) > p("s") p("e") p("s") p("s") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d7 d0  u(0x200B) > p("s") p("e") p("t") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d8 d0  u(0x200B) > p("o") p("i") p("t") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) d9 d0  u(0x200B) > p("n") p("o") p("v") p("e") p("n") p("t") p("a") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) > u(0x200B)  @2  d0 u(0x200B)  u(0x0020) p("e")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 d0 d0  u(0x200B) > p("c") p("e") p("m") / ^_  _  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("c") p("i") p("e") p("n") p("t") p("o")  u(0x0020) p("e")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d2 d0 d0  u(0x200B) > p("d") p("u") p("z") p("e") p("n") p("t") p("o") p("s") / ^_  _  _  _   _  ;
u(0x200B) d3 d0 d0  u(0x200B) > p("t") p("r") p("e") p("z") p("e") p("n") p("t") p("o") p("s") / ^_  _  _  _   _  ;
u(0x200B) d5 d0 d0  u(0x200B) > p("q") p("u") p("i") p("n") p("h") p("e") p("n") p("t") p("o") p("s") / ^_  _  _  _   _  ;
u(0x200B) dx d0 d0  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("c") p("i") p("e") p("n") p("t") p("o") p("s") / ^_  _  _  _   _  ;
u(0x200B) dx dd  dd  u(0x200B) > u(0x200B)  @2  d0 d0 u(0x200B)  u(0x0020) p("e")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
endif;

if (numt == 1 && lng == ROM)

u(0x200B) u(0x200B) d0  u(0x200B) > p("z") p("e") p("r") p("o") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("u") p("n") p("u") / ^_  _   _  ;
u(0x200B) d2 u(0x200B) u(0x200B) > p("d") p("o") p("i") / ^_  _  _  _  ;
u(0x200B) d2  u(0x200B) > p("d") p("o") p("u")  u(0x0103) / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("e") p("i") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("p") p("a") p("t") p("r") p("u") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("c") p("i") p("n") p("c") p("i") / ^_  _   _  ;
u(0x200B) d6 u(0x200B) u(0x200B) >  u(0x0219) p("a") p("s") p("e") / ^_  _  _  _  ;
u(0x200B) d6  u(0x200B) >  u(0x0219) p("a") p("i") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) >  u(0x0219) p("a") p("p") p("t") p("e") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("p") p("t") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("o") p("u")  u(0x0103) / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("z") p("e") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("u") p("n") p("s") p("p") p("r") p("e") p("z") p("e") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("d") p("o") p("i") p("s") p("p") p("r") p("e") p("z") p("e") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("p") p("a") p("i") p("s") p("p") p("r") p("e") p("z") p("e") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("s") p("p") p("r") p("e") p("z") p("e") p("c") p("e") / ^_  _  _   _  ;
u(0x200B) dx d0  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("z") p("e") p("c") p("i") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) > u(0x200B)  @2  d0 u(0x200B)  u(0x0020)  u(0x0219) p("i")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("o")  u(0x0020) p("s") p("u") p("t")  u(0x0103)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("s") p("u") p("t") p("e")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) > p("o")  u(0x0020) p("m") p("i") p("e")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == RUS)

u(0x200B) u(0x200B) d0  u(0x200B) >  u(0x043D)  u(0x043E)  u(0x043B)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) >  u(0x043E)  u(0x0434)  u(0x0438)  u(0x043D) / ^_  _   _  ;
u(0x200B) d2 u(0x200B) u(0x200B) >  u(0x0434)  u(0x0432)  u(0x0430) / ^_  _  _  _  ;
u(0x200B) d2  u(0x200B) >  u(0x0434)  u(0x0432)  u(0x0435) / ^_  _   _  ;
u(0x200B) d3  u(0x200B) >  u(0x0442)  u(0x0440)  u(0x0438) / ^_  _   _  ;
u(0x200B) d4  u(0x200B) >  u(0x0447)  u(0x0435)  u(0x0442)  u(0x044B)  u(0x0440)  u(0x0435) / ^_  _   _  ;
u(0x200B) d5  u(0x200B) >  u(0x043F)  u(0x044F)  u(0x0442)  u(0x044C) / ^_  _   _  ;
u(0x200B) d6  u(0x200B) >  u(0x0448)  u(0x0435)  u(0x0441)  u(0x0442)  u(0x044C) / ^_  _   _  ;
u(0x200B) d7  u(0x200B) >  u(0x0441)  u(0x0435)  u(0x043C)  u(0x044C) / ^_  _   _  ;
u(0x200B) d8  u(0x200B) >  u(0x0432)  u(0x043E)  u(0x0441)  u(0x0435)  u(0x043C)  u(0x044C) / ^_  _   _  ;
u(0x200B) d9  u(0x200B) >  u(0x0434)  u(0x0435)  u(0x0432)  u(0x044F)  u(0x0442)  u(0x044C) / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) >  u(0x0434)  u(0x0435)  u(0x0441)  u(0x044F)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) >  u(0x043E)  u(0x0434)  u(0x0438)  u(0x043D)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) >  u(0x0434)  u(0x0432)  u(0x0435)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) >  u(0x0442)  u(0x0440)  u(0x0438)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) >  u(0x0447)  u(0x0435)  u(0x0442)  u(0x044B)  u(0x0440)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) >  u(0x043F)  u(0x044F)  u(0x0442)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) >  u(0x0448)  u(0x0435)  u(0x0441)  u(0x0442)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d7  u(0x200B) >  u(0x0441)  u(0x0435)  u(0x043C)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d8  u(0x200B) >  u(0x0432)  u(0x043E)  u(0x0441)  u(0x0435)  u(0x043C)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) >  u(0x0434)  u(0x0435)  u(0x0432)  u(0x044F)  u(0x0442)  u(0x043D)  u(0x0430)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C) / ^_  _  _   _  ;
u(0x200B) (d2,d3) dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B)  u(0x0434)  u(0x0446)  u(0x0430)  u(0x0442)  u(0x044C)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) >  u(0x0441)  u(0x043E)  u(0x0440)  u(0x043E)  u(0x043A)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) >  u(0x0434)  u(0x0435)  u(0x0432)  u(0x044F)  u(0x043D)  u(0x043E)  u(0x0441)  u(0x0442)  u(0x043E)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0434)  u(0x0435)  u(0x0441)  u(0x044F)  u(0x0442)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) >  u(0x0441)  u(0x0442)  u(0x043E)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d2 dd  dd  u(0x200B) >  u(0x0434)  u(0x0432)  u(0x0435)  u(0x0441)  u(0x0442)  u(0x0438)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) (d3,d4) dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0441)  u(0x0442)  u(0x0430)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0441)  u(0x043E)  u(0x0442)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) >  u(0x043E)  u(0x0434)  u(0x043D)  u(0x0430)  u(0x0020)  u(0x0442)  u(0x044B)  u(0x0441)  u(0x044F)  u(0x0447)  u(0x0430)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) (d2,d3,d4) dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020)  u(0x0442)  u(0x044B)  u(0x0441)  u(0x044F)  u(0x0447)  u(0x0438)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) (d0,d2,d3,d4,d5,d6,d7,d8,d9) (d2,d3,d4) dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020)  u(0x0442)  u(0x044B)  u(0x0441)  u(0x044F)  u(0x0447)  u(0x0438)  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) (d2,d3,d4) dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020)  u(0x0442)  u(0x044B)  u(0x0441)  u(0x044F)  u(0x0447)  u(0x0438)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx (d0,d2,d3,d4,d5,d6,d7,d8,d9) (d2,d3,d4) dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020)  u(0x0442)  u(0x044B)  u(0x0441)  u(0x044F)  u(0x0447)  u(0x0438)  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020)  u(0x0442)  u(0x044B)  u(0x0441)  u(0x044F)  u(0x0447)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020)  u(0x0442)  u(0x044B)  u(0x0441)  u(0x044F)  u(0x0447)  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020)  u(0x0442)  u(0x044B)  u(0x0441)  u(0x044F)  u(0x0447)  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) >  u(0x043E)  u(0x0434)  u(0x0438)  u(0x043D)  u(0x0020)  u(0x043C)  u(0x0438)  u(0x043B)  u(0x043B)  u(0x0438)  u(0x043E)  u(0x043D)  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020)  u(0x043C)  u(0x0438)  u(0x043B)  u(0x043B)  u(0x0438)  u(0x043E)  u(0x043D)  u(0x043E)  u(0x0432)  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020)  u(0x043C)  u(0x0438)  u(0x043B)  u(0x043B)  u(0x0438)  u(0x043E)  u(0x043D)  u(0x043E)  u(0x0432)  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020)  u(0x043C)  u(0x0438)  u(0x043B)  u(0x043B)  u(0x0438)  u(0x043E)  u(0x043D)  u(0x043E)  u(0x0432)  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == SRPL)
u(0x200B) u(0x200B) d0  u(0x200B) > p("n") p("u") p("l") p("a") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("j") p("e") p("d") p("a") p("n") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("d") p("v") p("a") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("i") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) >  u(0x010D) p("e") p("t") p("i") p("r") p("i") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("p") p("e") p("t") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) >  u(0x0161) p("e") p("s") p("t") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("d") p("a") p("m") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("s") p("a") p("m") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("d") p("e") p("v") p("e") p("t") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("e") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("j") p("e") p("d") p("a") p("n") p("a") p("e") p("s") p("t") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) >  u(0x010D) p("e") p("t") p("r") p("n") p("a") p("e") p("s") p("t") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) >  u(0x0161) p("e") p("s") p("n") p("a") p("e") p("s") p("t") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("n") p("a") p("e") p("s") p("t") / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) >  u(0x010D) p("e") p("t") p("r") p("d") p("e") p("s") p("e") p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d5 dd  u(0x200B) > p("p") p("e") p("d") p("e") p("s") p("e") p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d6 dd  u(0x200B) >  u(0x0161) p("e") p("z") p("d") p("e") p("s") p("e") p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) > p("d") p("e") p("v") p("e") p("d") p("e") p("s") p("e") p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx d0  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("d") p("e") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("d") p("e") p("s") p("e") p("t")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("s") p("t") p("o")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d2 dd  dd  u(0x200B) > p("d") p("v") p("e") p("s") p("t") p("a")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d3 dd  dd  u(0x200B) > p("t") p("r") p("i") p("s") p("t") p("a")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("s") p("t") p("o")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd  dd  dd  u(0x200B) > p("h") p("i") p("l") p("j") p("a") p("d") p("u")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) d2 dd  dd  dd  u(0x200B) > p("d") p("v") p("e")  u(0x0020) p("h") p("i") p("l") p("j") p("a") p("d") p("e")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) (d3,d4) dd  dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("h") p("i") p("l") p("j") p("a") p("d") p("e")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
endif;
if (numt == 1 && lng == SLV)

u(0x200B) u(0x200B) d0  u(0x200B) > p("n") p("i")  u(0x010D) / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("e") p("n") p("a") / ^_  _   _  ;
u(0x200B) d2 u(0x200B) u(0x200B) > p("d") p("v") p("e") / ^_  _  _  _  ;
u(0x200B) d2  u(0x200B) > p("d") p("v") p("a") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("i") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) >  u(0x0161) p("t") p("i") p("r") p("i") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("p") p("e") p("t") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) >  u(0x0161) p("e") p("s") p("t") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("e") p("d") p("e") p("m") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("o") p("s") p("e") p("m") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("d") p("e") p("v") p("e") p("t") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("d") p("e") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("e") p("n") p("a") p("j") p("s") p("t") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("n") p("a") p("j") p("s") p("t") / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("d") p("v") p("a") p("j") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("i") p("n") p("d") p("v") p("a") p("j") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) dx d0  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("d") p("e") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @3 u(0x200B)  p("i") p("n")  u(0x200B) @2 u(0x200B)  p("d") p("e") p("s") p("e") p("t") / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("s") p("t") p("o")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d2 dd  dd  u(0x200B) > p("d") p("v") p("e") p("s") p("t") p("o")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("s") p("t") p("o")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd  dd  dd  u(0x200B) > p("t") p("i") p("s") p("o")  u(0x010D)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) dx dd  dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("t") p("i") p("s") p("o")  u(0x010D)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) dx dd dd  dd  dd  u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("t") p("i") p("s") p("o")  u(0x010D)  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _   _   _   _  ;
u(0x200B) dx dd dd dd  dd  dd  u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("t") p("i") p("s") p("o")  u(0x010D)  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _   _   _   _  ;
u(0x200B) d1 dd dd dd dd dd dd u(0x200B) > p("m") p("i") p("l") p("i") p("j") p("o") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) (d2,d3,d4) dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("j") p("o") p("n") p("a")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("j") p("o") p("n") p("o") p("v")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("j") p("o") p("n") p("o") p("v")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("i") p("j") p("o") p("n") p("o") p("v")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == SRB)
u(0x200B) u(0x200B) d0  u(0x200B) >  u(0x043D)  u(0x0443)  u(0x043B)  u(0x0430) / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) >  u(0x0458)  u(0x0435)  u(0x0434)  u(0x0430)  u(0x043D) / ^_  _   _  ;
u(0x200B) d2  u(0x200B) >  u(0x0434)  u(0x0432)  u(0x0430) / ^_  _   _  ;
u(0x200B) d3  u(0x200B) >  u(0x0442)  u(0x0440)  u(0x0438) / ^_  _   _  ;
u(0x200B) d4  u(0x200B) >  u(0x0447)  u(0x0435)  u(0x0442)  u(0x0438)  u(0x0440)  u(0x0438) / ^_  _   _  ;
u(0x200B) d5  u(0x200B) >  u(0x043F)  u(0x0435)  u(0x0442) / ^_  _   _  ;
u(0x200B) d6  u(0x200B) >  u(0x0448)  u(0x0435)  u(0x0441)  u(0x0442) / ^_  _   _  ;
u(0x200B) d7  u(0x200B) >  u(0x0441)  u(0x0435)  u(0x0434)  u(0x0430)  u(0x043C) / ^_  _   _  ;
u(0x200B) d8  u(0x200B) >  u(0x043E)  u(0x0441)  u(0x0430)  u(0x043C) / ^_  _   _  ;
u(0x200B) d9  u(0x200B) >  u(0x0434)  u(0x0435)  u(0x0432)  u(0x0435)  u(0x0442) / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) >  u(0x0434)  u(0x0435)  u(0x0441)  u(0x0435)  u(0x0442) / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) >  u(0x0458)  u(0x0435)  u(0x0434)  u(0x0430)  u(0x043D)  u(0x0430)  u(0x0435)  u(0x0441)  u(0x0442) / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) >  u(0x0447)  u(0x0435)  u(0x0442)  u(0x0440)  u(0x043D)  u(0x0430)  u(0x0435)  u(0x0441)  u(0x0442) / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) >  u(0x0448)  u(0x0435)  u(0x0441)  u(0x043D)  u(0x0430)  u(0x0435)  u(0x0441)  u(0x0442) / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) >  u(0x200B) @3 u(0x200B)   u(0x043D)  u(0x0430)  u(0x0435)  u(0x0441)  u(0x0442) / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) >  u(0x0447)  u(0x0435)  u(0x0442)  u(0x0440)  u(0x0434)  u(0x0435)  u(0x0441)  u(0x0435)  u(0x0442)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d5 dd  u(0x200B) >  u(0x043F)  u(0x0435)  u(0x0434)  u(0x0435)  u(0x0441)  u(0x0435)  u(0x0442)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d6 dd  u(0x200B) >  u(0x0448)  u(0x0435)  u(0x0437)  u(0x0434)  u(0x0435)  u(0x0441)  u(0x0435)  u(0x0442)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) >  u(0x0434)  u(0x0435)  u(0x0432)  u(0x0435)  u(0x0434)  u(0x0435)  u(0x0441)  u(0x0435)  u(0x0442)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx d0  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0434)  u(0x0435)  u(0x0441)  u(0x0435)  u(0x0442) / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0434)  u(0x0435)  u(0x0441)  u(0x0435)  u(0x0442)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) >  u(0x0441)  u(0x0442)  u(0x043E)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d2 dd  dd  u(0x200B) >  u(0x0434)  u(0x0432)  u(0x0435)  u(0x0441)  u(0x0442)  u(0x0430)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d3 dd  dd  u(0x200B) >  u(0x0442)  u(0x0440)  u(0x0438)  u(0x0441)  u(0x0442)  u(0x0430)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0441)  u(0x0442)  u(0x043E)  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd  dd  dd  u(0x200B) >  u(0x0445)  u(0x0438)  u(0x0459)  u(0x0430)  u(0x0434)  u(0x0443)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) d2 dd  dd  dd  u(0x200B) >  u(0x0434)  u(0x0432)  u(0x0435)  u(0x0020)  u(0x0445)  u(0x0438)  u(0x0459)  u(0x0430)  u(0x0434)  u(0x0435)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) (d3,d4) dd  dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020)  u(0x0445)  u(0x0438)  u(0x0459)  u(0x0430)  u(0x0434)  u(0x0435)  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
endif;
if (numt == 1 && lng == SVE)

u(0x200B) u(0x200B) d0  u(0x200B) > p("n") p("o") p("l") p("l") / ^_  _  _   _  ;
u(0x200B) u(0x200B) d1 u(0x200B) u(0x200B) > p("e") p("t") p("t") / ^_  _  _  _  _  ;
u(0x200B) u(0x200B) d1  u(0x200B) > p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("e") p("t") p("t") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("t") p("v")  u(0x00E5) / ^_  _   _  ;
u(0x200B) d3  u(0x200B) > p("t") p("r") p("e") / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("f") p("y") p("r") p("a") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("f") p("e") p("m") / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("s") p("e") p("x") / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("s") p("j") p("u") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) >  u(0x00E5) p("t") p("t") p("a") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("n") p("i") p("o") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("t") p("i") p("o") / ^_  _  _   _  ;
u(0x200B) d1 d1  u(0x200B) > p("e") p("l") p("v") p("a") / ^_  _  _   _  ;
u(0x200B) d1 d2  u(0x200B) > p("t") p("o") p("l") p("v") / ^_  _  _   _  ;
u(0x200B) d1 d3  u(0x200B) > p("t") p("r") p("e") p("t") p("t") p("o") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d4  u(0x200B) > p("f") p("j") p("o") p("r") p("t") p("o") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d5  u(0x200B) > p("f") p("e") p("m") p("t") p("o") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d6  u(0x200B) > p("s") p("e") p("x") p("t") p("o") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d7  u(0x200B) > p("s") p("j") p("u") p("t") p("t") p("o") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d8  u(0x200B) > p("a") p("r") p("t") p("o") p("n") / ^_  _  _   _  ;
u(0x200B) d1 d9  u(0x200B) > p("n") p("i") p("t") p("t") p("o") p("n") / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) > p("t") p("j") p("u") p("g") p("o")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d3 dd  u(0x200B) > p("t") p("r") p("e") p("t") p("t") p("i") p("o")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) > p("f") p("y") p("r") p("t") p("i") p("o")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d7 dd  u(0x200B) > p("s") p("j") p("u") p("t") p("t") p("i") p("o")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d8 dd  u(0x200B) >  u(0x00E5) p("t") p("t") p("i") p("o")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) > p("n") p("i") p("t") p("t") p("i") p("o")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx dd  u(0x200B) >  u(0x200B) @2 u(0x200B)  p("t") p("i") p("o")  u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) dx dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B) p("h") p("u") p("n") p("d") p("r") p("a")  u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B) p("u") p("s") p("e") p("n")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) (d0,d2,d3,d4,d5,d6,d7,d8,d9) d1 dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x200B) p("u") p("s") p("e") p("n")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) d1 dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x200B) p("u") p("s") p("e") p("n")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx (d0,d2,d3,d4,d5,d6,d7,d8,d9) d1 dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x200B) p("u") p("s") p("e") p("n")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)  p("t") p("u") p("s") p("e") p("n")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)  p("t") p("u") p("s") p("e") p("n")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)  p("t") p("u") p("s") p("e") p("n")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
endif;
if (numt == 1 && lng == TRK)

u(0x200B) u(0x200B) d0  u(0x200B) > p("s")  u(0x0131) p("f")  u(0x0131) p("r") / ^_  _  _   _  ;
u(0x200B) d1  u(0x200B) > p("b") p("i") p("r") / ^_  _   _  ;
u(0x200B) d2  u(0x200B) > p("i") p("k") p("i") / ^_  _   _  ;
u(0x200B) d3  u(0x200B) >  u(0x00FC)  u(0x00E7) / ^_  _   _  ;
u(0x200B) d4  u(0x200B) > p("d")  u(0x00F6) p("r") p("t") / ^_  _   _  ;
u(0x200B) d5  u(0x200B) > p("b") p("e")  u(0x015F) / ^_  _   _  ;
u(0x200B) d6  u(0x200B) > p("a") p("l") p("t")  u(0x0131) / ^_  _   _  ;
u(0x200B) d7  u(0x200B) > p("y") p("e") p("d") p("i") / ^_  _   _  ;
u(0x200B) d8  u(0x200B) > p("s") p("e") p("k") p("i") p("z") / ^_  _   _  ;
u(0x200B) d9  u(0x200B) > p("d") p("o") p("k") p("u") p("z") / ^_  _   _  ;
u(0x200B) d1 d0  u(0x200B) > p("o") p("n") / ^_  _  _   _  ;
u(0x200B) d1 dd  u(0x200B) > p("o") p("n")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d2 d0  u(0x200B) > p("y") p("i") p("r") p("m") p("i") / ^_  _  _   _  ;
u(0x200B) d2 dd  u(0x200B) > p("y") p("i") p("r") p("m") p("i")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d3 d0  u(0x200B) > p("o") p("t") p("u") p("z") / ^_  _  _   _  ;
u(0x200B) d3 dd  u(0x200B) > p("o") p("t") p("u") p("z")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d4 d0  u(0x200B) > p("k")  u(0x0131) p("r") p("k") / ^_  _  _   _  ;
u(0x200B) d4 dd  u(0x200B) > p("k")  u(0x0131) p("r") p("k")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d5 d0  u(0x200B) > p("e") p("l") p("l") p("i") / ^_  _  _   _  ;
u(0x200B) d5 dd  u(0x200B) > p("e") p("l") p("l") p("i")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d6 d0  u(0x200B) > p("a") p("l") p("t") p("m")  u(0x0131)  u(0x015F) / ^_  _  _   _  ;
u(0x200B) d6 dd  u(0x200B) > p("a") p("l") p("t") p("m")  u(0x0131)  u(0x015F)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d7 d0  u(0x200B) > p("y") p("e") p("t") p("m") p("i")  u(0x015F) / ^_  _  _   _  ;
u(0x200B) d7 dd  u(0x200B) > p("y") p("e") p("t") p("m") p("i")  u(0x015F)  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d8 d0  u(0x200B) > p("s") p("e") p("k") p("s") p("e") p("n") / ^_  _  _   _  ;
u(0x200B) d8 dd  u(0x200B) > p("s") p("e") p("k") p("s") p("e") p("n")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d9 d0  u(0x200B) > p("d") p("o") p("k") p("s") p("a") p("n") / ^_  _  _   _  ;
u(0x200B) d9 dd  u(0x200B) > p("d") p("o") p("k") p("s") p("a") p("n")  u(0x003A) u(0x003A) @3 u(0x200B) @3 u(0x200B) / ^_  _  _   _  ;
u(0x200B) d1 dd  dd  u(0x200B) > p("y")  u(0x00FC) p("z")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) (d2,d3,d4,d5,d6,d7,d8,d9) dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("y")  u(0x00FC) p("z")  u(0x003A) u(0x003A) @3 @4 u(0x200B) @3 @4 u(0x200B) / ^_  _  _   _   _  ;
u(0x200B) d1 dd  dd  dd  u(0x200B) > p("b") p("i") p("n")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _   _   _   _  ;
u(0x200B) dx (d1,d2,d3,d4,d5,d6,d7,d8,d9) dd  dd  u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("b") p("i") p("n")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _   _   _  ;
u(0x200B) dx dd (d1,d2,d3,d4,d5,d6,d7,d8,d9) dd  dd  u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("b") p("i") p("n")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _   _   _  ;
u(0x200B) dx dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("b") p("i") p("n")  u(0x003A) u(0x003A) @3 @4 @5 u(0x200B) @3 @4 @5 u(0x200B) / ^_  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("b") p("i") p("n")  u(0x003A) u(0x003A) @4 @5 @6 u(0x200B) @4 @5 @6 u(0x200B) / ^_  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("b") p("i") p("n")  u(0x003A) u(0x003A) @5 @6 @7 u(0x200B) @5 @6 @7 u(0x200B) / ^_  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("y") p("o") p("n")  u(0x003A) u(0x003A) @3 @4 @5 @6 @7 @8 u(0x200B) @3 @4 @5 @6 @7 @8 u(0x200B) / ^_  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("y") p("o") p("n")  u(0x003A) u(0x003A) @4 @5 @6 @7 @8 @9 u(0x200B) @4 @5 @6 @7 @8 @9 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  ;
u(0x200B) dx dd dd dd dd dd dd dd dd u(0x200B) >  u(0x200B) @2 @3 @4 u(0x200B)   u(0x0020) p("m") p("i") p("l") p("y") p("o") p("n")  u(0x003A) u(0x003A) @5 @6 @7 @8 @9 @10 u(0x200B) @5 @6 @7 @8 @9 @10 u(0x200B) / ^_  _  _  _  _  _  _  _  _  _  _  ;
endif;


if (thou > 0 && !numt)

cdecsep dd dd dd dd > @1 @2 @3 @4 u(0x200B) @5 / _ ^_ _ _ _;

dd dd dd dd dd dd dd dd dd dd dd dd dd > @1 u(0x202F) @2 @3 @4 u(0x202F) @5 @6 @7 u(0x202F) @8 @9 @10 u(0x202F) @11 @12 @13 / ^_ _ _ _ _ _ _ _ _ _ _ _ _ ;
dd dd dd dd dd dd dd dd dd dd dd dd > @1 @2 @3 u(0x202F) @4 @5 @6 u(0x202F) @7 @8 @9 u(0x202F) @10 @11 @12 / ^_ _ _ _ _ _ _ _ _ _ _ _;
dd dd dd dd dd dd dd dd dd dd dd > @1 @2 u(0x202F) @3 @4 @5 u(0x202F) @6 @7 @8 u(0x202f) @9 @10 @11 / ^_ _ _ _ _ _ _ _ _ _ _;
dd dd dd dd dd dd dd dd dd dd > @1 u(0x202F) @2 @3 @4 u(0x202F) @5 @6 @7 u(0x202F) @8 @9 @10 / ^ _ _ _ _ _ _ _ _ _ _;
dd dd dd dd dd dd dd dd dd > @1 @2 @3 u(0x202F) @4 @5 @6 u(0x202F) @7 @8 @9 / ^_ _ _ _ _ _ _ _ _; 
dd dd dd dd dd dd dd dd > @1 @2 u(0x202F) @3 @4 @5 u(0x202F) @6 @7 @8 / ^_ _ _ _ _ _ _ _; 
dd dd dd dd dd dd dd > @1 u(0x202F) @2 @3 @4 u(0x202F) @5 @6 @7 / ^_ _ _ _ _ _ _; 
dd dd dd dd dd dd > @1 @2 @3 u(0x202F) @4 @5 @6 / ^_ _ _ _ _ _; 
dd dd dd dd dd > @1 @2 u(0x202F) @3 @4 @5 / ^_ _ _ _ _; 

  if (thou == 2)
	dd dd dd dd > @1 u(0x202F) @2 @3 @4 / ^_ _ _ _; 
  endif;

endif;

if (arti==1 && numt == 0 && lng == HUN)

u(0x200B) ad1 _ > p("z") u(0x0020) @2 / ^ _ _ _;
u(0x200B) ad5 _ > p("z") u(0x0020) @2 / ^ _ _ _;
u(0x200B) add > u(0x0020) @2 / _ ^_;
u(0x200B) ad5 add _ > p("z") u(0x0020) @2 @3 / ^ _ _ _ _;
u(0x200B) add add > u(0x0020) @2 @3 / _ _ ^_;
u(0x200B) ad5 add add > p("z") u(0x0020) @2 @3 @4 / ^ _ _ _ _ ;
u(0x200B) add add add > u(0x0020) @2 @3 @4 / _ _ ^_ _;
u(0x200B) ad1 add add add > p("z") u(0x0020) @2 @3 @4 @5 / _ _ ^_ _ _;
u(0x200B) ad5 add add add > p("z") u(0x0020) @2 @3 @4 @5 / _ _ ^ _ _ _;
u(0x200B) add add add add > u(0x0020) @2 @3 @4 @5 / _ _ ^_ _ _;
u(0x200B) ad5 add add add add _ > p("z") u(0x0020) @2 @3 @4 @5 @6 / ^ _ _ _ _ _ _ _;
u(0x200B) add add add add add > u(0x0020) @2 @3 @4 @5 @6;
u(0x200B) ad5 add add add add add _ > p("z") u(0x0020) @2 @3 @4 @5 @6 @7 / ^ _ _ _ _ _ _ _ _ ;
u(0x200B) add add add add add add > u(0x0020) @2 @3 @4 @5 @6 @7;
u(0x200B) ad1 add add add add add add _ > p("z") u(0x0020) @2 @3 @4 @5 @6 @7 @8 / ^ _ _ _ _ _ _ _ _ _ ;
u(0x200B) ad5 add add add add add add _ > p("z") u(0x0020) @2 @3 @4 @5 @6 @7 @8 / ^ _ _ _ _ _ _ _ _ _ ;
u(0x200B) add add add add add add add > u(0x0020) @2 @3 @4 @5 @6 @7 @8;

add > @2 / ANY _;
add > p("a") u(0x200B) @1 / ^_;

endif;

if (numt == 3)
  if (vari == 0)
	d1 dd > @1 @2 / _ _ dd;
	d1 dd > @1 @2 p("t") p("h");
	dd > @1 / _ dd;
	d1 > @1 p("s") p("t");
	d2 > @1 p("n") p("d");
	d3 > @1 p("r") p("d");
	dd > @1 p("t") p("h");
  else
	d1 dd > @1 @2 / _ _ dd;
	d1 dd > @1 @2 p("t.superior") p("h.superior");
	dd > @1 / _ dd;
	d1 > @1 p("s.superior") p("t.superior");
	d2 > @1 p("n.superior") p("d.superior");
	d3 > @1 p("r.superior") p("d.superior");
	dd > @1 p("t.superior") p("h.superior");
 endif;

endif;

if (foot > 0)
  if (foot == 2 || lng == HUN)
    if (!algn)
	d1 > asterisk;
	d2 > asterisk asterisk;
	d3 > asterisk asterisk asterisk;
	d4 > dagger;
	d5 > dagger dagger;
	d6 > dagger dagger dagger;
	d7 > daggerdbl;
	d8 > daggerdbl daggerdbl;
	d9 > daggerdbl daggerdbl daggerdbl;
    else
	d1 _ > ZWSP asterisk {user1 = true} / ^ _ _;
	d2 _ _ > ZWSP asterisk {user1 = true} asterisk / ^ _ _ _;
	d3 _ _ _ > ZWSP asterisk {user1 = true} asterisk asterisk;
	d4 _ > ZWSP dagger {user1 = true} / ^ _ _;
	d5 _ _ > ZWSP dagger {user1 = true} dagger / ^ _ _ _;
	d6 _ _ _ > ZWSP dagger {user1 = true} dagger dagger;
	d7 _ > ZWSP daggerdbl {user1 = true} / ^ _ _;
	d8 _ _ > ZWSP daggerdbl {user1 = true} daggerdbl / ^ _ _ _;
	d9 _ _ _ > ZWSP daggerdbl {user1 = true} daggerdbl daggerdbl;
    endif;
  else
    if (!algn)
	d1 > asterisk;
	d2 > dagger;
	d3 > daggerdbl;
	d4 > u(0x00A7);
	d5 > asterisk asterisk;
	d6 > dagger dagger;
	d7 > daggerdbl daggerdbl;
	d8 > u(0x00A7) u(0x00A7);
	d9 > asterisk asterisk asterisk;
	d1 d0 > dagger dagger dagger;
	d1 d1 > daggerdbl daggerdbl daggerdbl;
	d1 d2 > u(0x00A7) u(0x00A7) u(0x00A7);
    else
	d1 _ > ZWSP asterisk {user1 = true} / ^ _ _;
	d2 _ > ZWSP dagger {user1 = true} / ^ _ _;
	d3 _ > ZWSP daggerdbl {user1 = true} / ^ _ _;
	d4 _ > ZWSP u(0x00A7) {user1 = true} / ^ _ _;
	d5 _ _ > ZWSP asterisk {user1 = true} asterisk / ^ _ _ _;
	d6 _ _ > ZWSP dagger {user1 = true} dagger / ^ _ _ _;
	d7 _ _ > ZWSP daggerdbl {user1 = true} daggerdbl / ^ _ _ _;
	d8 _ _ > ZWSP u(0x00A7) {user1 = true} u(0x00A7) / ^ _ _ _;
	d9 _ _ _ > ZWSP asterisk {user1 = true} asterisk asterisk / ^ _ _ _ _;
	d1 d0 _ _ > ZWSP dagger {user1 = true} dagger dagger / ^ _ _ _ _;
	d1 d1 _ _ > ZWSP daggerdbl {user1 = true} daggerdbl daggerdbl / ^ _ _ _ _;
	d1 d2 _ _ > ZWSP u(0x00A7) {user1 = true} u(0x00A7) u(0x00A7) / ^ _ _ _ _;
    endif;
  endif;
endif;

if (algn && !foot)	
	numbers numbers numbers _ > ZWSP @1 { user1 = true } @2 { user1 = true } @3 { user1 = true } / ^_ { user1 == false } _ _ _;
	numbers numbers _ > ZWSP @1 { user1 = true } @2 { user1 = true} / ^_ { user1 == false } _ _;
	numbers _ > ZWSP @1 { user1 = true } / ^ _ { user1 == false } _;

// optional fix of spaces after bullets in LibreOffice
	u(0x2022) _ > ZWSP @1 { user1 = true } / ^ _ { user1 == false } _;

endif;

"""

feat_linlib = """
caps { id = "caps"; name.LG_USENG = string ("'caps' Capitalization"); 
	settings {
		none {value = 0; name.LG_USENG = string("None"); }
		first { value = 1; name.LG_USENG = string("Capitalized"); }
		all { value = 2; name.LG_USENG = string("Uppercase"); }
		wordparts { value = 3; name.LG_USENG = string("Capitalized words and word parts"); }
		title { value = 4; name.LG_USENG = string("Capitalized words"); }
	}
}
ligc {id = "ligc"; default = 1; name.LG_USENG="'ligc' Ligature correction at hyphenation";}
"""

glyph_linlib = """
//csc123 = (csc1, csc2, csc3);
//csc123lig = (csc123, letters);
//csc123ligd = (csc123lig, 0x002D)
//csc123liga = (csc123ligd, 0x0020)

cnumsup = u(0x2070, 0x00B9, 0x00B2, 0x00B3, 0x2074.. 0x2079);
cnumsub = u(0x2080.. 0x2089);

dashes = u(0x2012.. 0x2015);
slashes = p("slash", "fraction");

smallcap_salt_A_1 = u(0x00E0.. 0x00E5, 0x0103, 0x0105);
smallcap_salt_A_2 = u(0x0300.. 0x0303, 0x0308, 0x030A, 0x0306, 0x0328);

righthang1 = p("hyphen", "period", "comma", "quoteleft", "quoteright", "colon", "semicolon", "quotedblleft", "quotedblright", "endash", "emdash", "question", "exclam");
righthang2 = u(0xE131 .. 0xE13D);
lefthang1 = p("quoteleft", "quoteright", "quotesinglbase", "quotedblleft", "quotedblright", "quotedblbase");
lefthang2 = u(0xE13E .. 0xE143);
"""

sub_linlib = """

// black-board letters

if (texm)
u(0x005C) p("m") p("a") p("t") p("h") p("b") p("b") u(0x007B) dblCap u(0x007D) > _ _ _ _ _ _ _ _ dblCap2 _;
u(0x005C) p("m") p("a") p("t") p("h") p("b") p("b") u(0x007B) dblCap diaD u(0x007D) > _ _ _ _ _ _ _ _ dblCap2 @10 _;
endif;

// non-French spacing: larger spaces (+33%) within sentences, 
// except after capital letter + punctuation and before lower letter

if (nfsp)
u(0x0020) > @3 {user6 = 1} / csc3 sentenceend ^ _ {user6 == 0} ANY;
u(0x0020) > @3 {user6 = 1} / sentenceend ^ _ {user6 == 0} csc1;
u(0x0020) _ _ _ > @2 {user6 = 1} u(0x200A) u(0x200A) u(0x200A) / sentenceend ^ _ {user6 == 0} _ _ _ ANY;
endif;

// larger spaces in capitalized text

if (caps==2)
u(0x0020) _ > @1 {user7 = 1} u(0x200A) / ^ _ {user7 == 0} _ANY;
endif;

// hyphen mark
if (hang)

(righthang1, lefthang1) > @2 { u_hang = 3 } / ANY ^ _ { u_hang == 0 } ANY ;
(righthang1, lefthang1) > @2 { u_hang = 1 } / ANY ^ _ { u_hang == 0 } ;
(righthang1, lefthang1) > @1 { u_hang = 2 } / ^_ { u_hang == 0 } ANY;

if (hang == 2)
p("hyphen") > u(0xE130) / ^ _ { u_hang == 0 };
else
righthang1 > righthang2 / ^ _ { u_hang == 0 || u_hang == 1 };
lefthang1 > lefthang2 / ^ _ { u_hang == 0 || u_hang == 2 };
endif;
endif;


// Dutch letter IJ

if (lng == NLD && caps != 2)
	p("I") p("J") > u(0x132 )_;

	if (liga && !sups)
		p("f") _ > f_corr ZWSP / _ _ p("i") p("j");
		p("f") p("f")  > ff_corr ZWSP / _ _ p("i") p("j");
	endif;
endif;

if (caps == title) // eg. Twenty-one
	if (smcp) 
		csc2 > csc2 / csc123ligd _;
	else
		csc1 > @ / csc123ligd _;
	endif;
	if (lng == NLD)
		p("i") p("j") > _ u(0x0132) / ^ _;
	endif;
	csc1 > csc3 {user3 = true} / ^_;
	csc2 > csc3 / ^_;
else if (caps == 2)	// eg. TWENTY-ONE
	csc1 > csc3 / ^_;
	csc2 > csc3 / ^_;
else if (caps == 3)	// eg. Twenty-One
	if (smcp) 
		csc1 > csc2 / csc123lig _;
	else
		csc1 > @ / csc123lig _;
	endif;
	if (lng == NLD)
		p("i") p("j") > _ u(0x0132) / ^ _;
	endif;
	csc1 > csc3 { user3 = true } / ^_ ;
	csc2 > csc3 / ^_;
else if (caps == first)	// eg. Hundred twenty-one
	if (smcp) 
		csc1 > csc2 / csc123liga _;
	else
		csc1 > @ / csc123liga _;
	endif;
	if (lng == NLD)
		p("i") p("j") > _ u(0x0132) / ^ _;
	endif;
	csc1 > csc3 { user3 = true } / ^_;
	csc2 > csc3 / ^_;
endif;

if (frac==1)

p("one") slashes p("four") > p("onequarter") / ^_ _ _ ;
p("one") slashes p("two") > p("onehalf") / ^_ _ _ ;
p("three") slashes p("four") > p("threequarters") / ^_ _ _ ;
p("one") slashes p("three") > p("onethird") / ^_ _ _ ;
p("two") slashes p("three") > p("twothirds") / ^_ _ _ ;

dd dd dd dd u(0x002F) dd > cnumsup cnumsup cnumsup cnumsup u(0x2044) cnumsub / ^_ _ _ _ _ _;
dd dd dd u(0x002F) dd > cnumsup cnumsup cnumsup u(0x2044) cnumsub / ^_ _ _ _ _;
dd dd u(0x002F) dd > cnumsup cnumsup u(0x2044) cnumsub / ^_ _ _ _;
dd u(0x002F) dd dd > cnumsup u(0x2044) cnumsub @4 / ^_ _ _;
dd u(0x002F) dd > cnumsup u(0x2044) cnumsub / ^_ _ _;

u(0x2044) cnumsub dd dd dd > u(0x2044) @2 cnumsub cnumsub cnumsub / ^_ _ _ _ _;
u(0x2044) cnumsub dd dd > u(0x2044) @2 cnumsub cnumsub / ^_ _ _ _;
u(0x2044) cnumsub dd > u(0x2044) @2 cnumsub / ^_ _ _;
endif;

if (frac==2)
dd dd dd u(0x002F) > cnumsup {user1=true} cnumsup cnumsup u(0x2015) / ^_ _ _ _ dd;
dd dd u(0x002F) > cnumsup {user1=true} cnumsup u(0x2014) / ^_ _ _ dd;
dd u(0x002F) > cnumsup {user1=true} u(0x2013) / ^_ _ dd;
dashes dd dd dd > u(0x2015) cnumsub cnumsub cnumsub {user1=true} / _ _ _ _;
u(0x2013) dd dd > u(0x2014) cnumsub cnumsub {user1=true} / ^_ _ _;
dashes dd dd > @1 cnumsub cnumsub {user1=true} / ^_ _ _;
dashes dd > @1 cnumsub {user1=true} / ^_ _;
endif;

if (dash)
	p("hyphen") > p("endash") / u(0x0020) _ u(0x0020);
	p("hyphen") > p("endash") / u(0x0020) _ p("comma");
	p("hyphen") > p("hyphen") / ANY _ u(0x0020);
	p("hyphen") > p("endash") / _ u(0x0020);
endif;

if (quot)

	if (lng==CSY || lng==HUN || lng==ROM)
		p("quotedbl") > p("quotedblbase") / u(0x0020) _ ANY;
		p("quotedbl") > p("quotedblbase") / p("parenleft") _ ANY;
	endif;

	if (lng==CSY || lng==DEU || lng==HUN || lng==PLK || lng==ROM || lng==SRB || lng==SRPL)
		p("quotedbl") > p("quotedblbase") / u(0x0020) _ ANY;
		p("quotedbl") > p("quotedblbase") / p("parenleft") _ ANY;
	else if (lng == AFK || lng == CAT || lng == ENG || lng==ESP || lng==NLD || lng==PTG || lng==TRK) 
		p("quotedbl") > p("quotedblleft") / u(0x0020) _ ANY;
		p("quotedbl") > p("quotedblleft") / p("parenleft") _ ANY;
	else if (lng == FIN || lng == SVE)
		p("quotedbl") > p("quotedblright") / u(0x0020) _ ANY;
		p("quotedbl") > p("quotedblright") / p("parenleft") _ ANY;
	endif;

	if (lng == AFK || lng == CAT || lng == ENG || lng == ESP || lng==HUN || lng == FIN || lng==NLD || lng == PLK || lng == PTG || lng==ROM || lng == SVE || lng == TRK)
		p("quotedbl") > p("quotedblright") / ANY _ punctsp;
	else if (lng == CSY || lng == DEU || lng == SRB || lng == SRPL)
		p("quotedbl") > p("quotedblleft") / ANY _ punctsp;
	endif;

	p("quotedbl") > p("quotedbl") / ANY _ ANY;

	if (lng==CSY || lng==DEU || lng==HUN || lng==PLK || lng==ROM || lng==SRB || lng==SRPL)
		p("quotedbl") > p("quotedblbase") / _ ANY;
	else if (lng == AFK || lng == CAT || lng == ENG || lng==ESP || lng==NLD || lng==PTG || lng==TRK) 
		p("quotedbl") > p("quotedblleft") / _ ANY;
	else if (lng == FIN || lng == SVE)
		p("quotedbl") > p("quotedblright") / _ ANY;
	endif;

	if (lng == AFK || lng == CAT || lng == ENG || lng == ESP || lng==HUN || lng == FIN || lng==NLD || lng == PLK || lng == PTG || lng==ROM || lng == SVE || lng == TRK)
		p("quotedbl") > p("quotedblright") / ANY _;
	else if (lng == CSY || lng == DEU || lng == SRB || lng == SRPL)
		p("quotedbl") > p("quotedblleft") / ANY _;
	endif;
endif;
"""



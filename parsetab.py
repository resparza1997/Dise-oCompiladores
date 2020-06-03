
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BraquetDer BraquetIzq Coma ConstanteChar ConstanteFloat ConstanteInt CorcheteDer CorcheteIzq Desde Entonces Escribe Funcion Hacer Hasta Haz Identificador Igual Lee Letrero Mientras OperadorLogico ParentecisDer ParentecisIzq Principal Programa PuntoComa Regresa Si SignoLogico SignoMultDiv SignoSumRest Sino Tipo TipoRetorno Var\n    programa            : Programa Identificador goto PuntoComa programaGlobal Principal popGoto ParentecisIzq ParentecisDer BraquetIzq estatutoVoid BraquetDer addEndProgram llamarMaquinaVirtual\n    llamarMaquinaVirtual :\n    programaGlobal      : variables definirFuncion addEndFunc programaGlobal\n                        | variables \n                        | definirFuncion addEndFunc programaGlobal\n                        | \n    \n    variables           : Var definirTipoVariable\n    \n    definirTipoVariable : Tipo definirVariable PuntoComa \n                        | Tipo definirVariable PuntoComa definirTipoVariable\n    \n    definirVariable     : tipoIdentificadorDeclaracion defineTipo\n                        | tipoIdentificadorDeclaracion Coma defineTipo definirVariable\n    \n    tipoIdentificadorDeclaracion    : Identificador\n                                    | arrayDeclaracion    \n    \n    arrayDeclaracion    : Identificador CorcheteIzq ConstanteInt validarInt CorcheteDer\n    \n    tipoIdentificador   : Identificador validarIdentificador\n                        | array\n    validarIdentificador :\n    array               : Identificador CorcheteIzq addLista asignarValor cerrarListaArray verArray CorcheteDer\n    cerrarListaArray :verArray :\n    definirFuncion      : Funcion TipoRetorno Identificador modificarFuncionActual ParentecisIzq parametrosDeclaracion ParentecisDer variablesLocales BraquetIzq estatutoVoid BraquetDer popVars\n                        | Funcion Tipo Identificador modificarFuncionActual ParentecisIzq parametrosDeclaracion ParentecisDer variablesLocales BraquetIzq estatuto validarRegresa BraquetDer popVars\n    validarRegresa :modificarFuncionActual :\n    parametrosDeclaracion   : parametros\n                            |\n    \n    parametros          : Tipo Identificador addVarParametro \n                        | Tipo Identificador addVarParametro Coma parametros\n    addVarParametro :\n    variablesLocales    : variables \n                        | \n    \n    estatuto            : asignacion noReturn estatuto \n                        | lectura noReturn estatuto \n                        | escritura noReturn estatuto \n                        | si noReturn estatuto \n                        | mientras noReturn estatuto \n                        | desde noReturn estatuto \n                        | llamarFuncion noReturn estatuto \n                        | regresa siReturn estatuto\n                        | \n    noReturn :siReturn :\n    estatutoVoid        : asignacion estatuto \n                        | lectura estatuto \n                        | escritura estatuto \n                        | si estatuto \n                        | mientras estatuto \n                        | desde estatuto \n                        | llamarFuncion estatuto \n                        | \n    \n    asignacion          : tipoIdentificador validarVariable iniciarListaDir Igual asignarValor validarDirArray PuntoComa\n    validarDirArray :iniciarListaDir :\n    asignarValor        : exprecionArismetica valorFinal\n                        | tipoIdentificador validarVariable\n                        | llamarFuncionAsignacion validarLlamada\n                        | ConstanteInt validarInt\n                        | ConstanteFloat validarFloat\n                        | ConstanteChar validarChar\n    validarLlamada :validarVariable :\n    llamarFuncion       : Identificador validarFuncion ParentecisIzq parametrosLlamada goSub asignarValorFuncion ParentecisDer PuntoComa\n    \n    llamarFuncionAsignacion       : Identificador validarFuncion ParentecisIzq parametrosLlamada goSub asignarValorFuncion ParentecisDer\n    asignarValorFuncion :goSub :validarFuncion :\n    parametrosLlamada   : valoresLlamada\n                        |  \n    \n    valoresLlamada      : addLista asignarValor paramFuncion cerrarListaArray\n                        | addLista asignarValor paramFuncion cerrarListaArray Coma valoresLlamada\n    paramFuncion :\n    exprecionArismetica : asignarMultDiv cuadruploSR SignoSumRest addOperador exprecionArismetica\n                        | asignarMultDiv cuadruploSR            \n    \n    asignarMultDiv      : asignarValorArismetico cuadruploMD SignoMultDiv addOperador asignarMultDiv\n                        | asignarValorArismetico cuadruploMD\n    \n    asignarValorArismetico  : valor addListaVariables\n                            | ParentecisIzq addLista estatuto cerrarLista ParentecisDer\n                            | ParentecisIzq addLista exprecionArismetica cerrarLista ParentecisDer\n    valorFinal :addListaVariables :addOperador :addLista :cerrarLista :\n    valor               : ConstanteInt validarInt\n                        | ConstanteFloat validarFloat\n                        | tipoIdentificador validarVariable\n                        | llamarFuncionAsignacion validarLlamada\n    \n    lectura             : Lee ParentecisIzq valoresLectura ParentecisDer PuntoComa\n    \n    valoresLectura      : tipoIdentificador cuadruploLectura\n                        | tipoIdentificador cuadruploLectura Coma valoresLectura\n    cuadruploLectura :\n    escritura           : Escribe ParentecisIzq definirEscritura ParentecisDer PuntoComa\n    \n    definirEscritura    : asignarValorEscritura cuadruploEscritura\n                        | asignarValorEscritura cuadruploEscritura Coma definirEscritura\n    \n    asignarValorEscritura   : exprecionArismetica valorFinal\n                            | tipoIdentificador validarVariable\n                            | llamarFuncionAsignacion validarLlamada\n                            | ConstanteChar validarChar\n    cuadruploEscritura :\n    si                  : Si ParentecisIzq exprecionLogica ParentecisDer gotoF Entonces BraquetIzq estatuto BraquetDer sino\n    \n    exprecionLogica     : asignarOperadorLogico cuadruploSignoLogico SignoLogico addOperadorLogico exprecionLogica\n                        | asignarOperadorLogico cuadruploSignoLogico\n    \n    asignarOperadorLogico   : asignarValor addVariableLogica cuadruploOperadorLogico OperadorLogico addOperadorLogico asignarOperadorLogico\n                            | asignarValor addVariableLogica cuadruploOperadorLogico \n    addVariableLogica :addOperadorLogico :\n    sino                : popGotoFs Sino goto BraquetIzq estatuto BraquetDer popGoto\n                        | popGotoF\n    \n    mientras            : Mientras ParentecisIzq gotoM exprecionLogica ParentecisDer gotoF Haz BraquetIzq estatuto BraquetDer popGotoFs popGotoM\n    \n    desde               : Desde tipoIdentificador validarIdDesde Igual asignarValor asignarDesde Hasta gotoM asignarValor comparaDesde gotoF Hacer BraquetIzq estatuto BraquetDer addUnoVariable popGotoFs popGotoM\n    validarIdDesde :asignarDesde :comparaDesde :addUnoVariable :\n    regresa             : Regresa ParentecisIzq asignarValor regresaCuadruplo ParentecisDer PuntoComa\n    regresaCuadruplo   :defineTipo :popVars :addEndFunc :addEndProgram :goto :popGoto :gotoM :popGotoM :gotoF :popGotoFs :popGotoF :cuadruploMD :cuadruploSR :cuadruploSignoLogico :cuadruploOperadorLogico :validarInt :validarFloat :validarChar :debugErrors :'
    
_lr_action_items = {'Programa':([0,],[2,]),'$end':([1,71,101,145,],[0,-120,-2,-1,]),'Identificador':([2,15,16,17,31,37,41,46,50,51,52,53,54,55,56,62,70,72,74,75,76,77,78,79,80,89,90,91,92,99,100,102,103,104,105,106,107,108,109,110,114,136,138,140,143,155,158,181,190,191,197,198,199,200,201,203,221,223,225,226,234,235,238,243,245,247,249,250,256,257,261,265,267,268,272,275,277,278,281,282,283,284,285,286,],[3,23,25,26,-117,23,48,66,48,48,48,48,48,48,48,94,-82,-41,-41,-41,-41,-41,-41,-41,-42,94,122,122,-123,-82,122,48,48,48,48,48,48,48,48,122,-82,122,48,48,122,122,195,122,-88,94,-92,122,-81,-82,-81,-106,122,122,122,-106,-115,-51,-82,48,122,-123,-62,-82,48,122,-127,-100,-108,-126,-124,-109,48,48,-122,-114,-107,-126,-124,-110,]),'PuntoComa':([3,4,21,22,23,24,30,42,63,64,69,121,122,123,124,125,126,130,131,132,133,134,135,156,159,165,167,168,169,170,174,175,176,177,178,179,189,196,212,213,219,231,233,236,237,239,240,242,252,260,270,],[-121,5,29,-117,-12,-13,-10,-11,-16,-14,-15,-129,-17,-128,-80,-132,-133,-79,-61,-60,-132,-133,-134,190,197,-73,-75,-76,-84,-85,-54,-55,-56,-57,-58,-59,-52,-60,234,235,-87,249,-18,-77,-78,-72,-61,-74,-86,-63,249,]),'Principal':([5,6,7,8,12,13,14,19,20,28,29,36,207,229,230,248,],[-6,11,-4,-119,-119,-6,-7,-6,-5,-3,-8,-9,-118,-21,-118,-22,]),'Var':([5,8,12,13,19,65,67,207,229,230,248,],[9,-119,-119,9,9,9,9,-118,-21,-118,-22,]),'Funcion':([5,7,8,12,13,14,19,29,36,207,229,230,248,],[10,10,-119,-119,10,-7,10,-8,-9,-118,-21,-118,-22,]),'Tipo':([9,10,29,39,40,139,],[15,17,15,46,46,46,]),'TipoRetorno':([10,],[16,]),'ParentecisIzq':([11,18,25,26,33,34,48,58,59,60,61,68,70,81,90,91,92,99,100,110,114,122,136,143,155,158,166,181,195,198,199,200,201,203,218,221,223,225,226,238,245,247,250,257,],[-122,27,-24,-24,39,40,-66,89,90,91,92,99,-82,110,114,114,-123,-82,114,114,-82,-66,114,114,114,114,200,114,-66,114,-81,-82,-81,-106,238,114,114,114,-106,-82,114,-123,-82,114,]),'BraquetIzq':([14,29,35,36,65,67,95,96,98,224,246,271,274,276,],[-7,-8,41,-9,-31,-31,138,-30,140,243,256,-121,277,278,]),'Coma':([22,23,24,63,64,66,69,94,97,113,116,117,118,119,120,121,122,123,124,125,126,130,131,132,133,134,135,157,160,161,162,163,164,165,167,168,169,170,174,175,176,177,178,179,186,196,210,219,232,233,236,237,239,240,242,252,260,],[31,-12,-13,-16,-14,-29,-15,-17,139,-91,-99,-79,-61,-60,-134,-129,-17,-128,-80,-132,-133,-79,-61,-60,-132,-133,-134,191,198,-95,-86,-87,-98,-73,-75,-76,-84,-85,-54,-55,-56,-57,-58,-59,-71,-60,-19,-87,250,-18,-77,-78,-72,-61,-74,-86,-63,]),'CorcheteIzq':([23,48,94,122,195,],[32,70,70,70,70,]),'ParentecisDer':([27,39,40,44,45,47,63,66,69,72,74,75,76,77,78,79,80,94,97,99,102,103,104,105,106,107,108,109,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,141,142,146,147,148,149,150,151,152,153,154,157,158,160,161,162,163,164,165,167,168,169,170,172,173,174,175,176,177,178,179,180,183,185,186,188,190,192,193,194,195,196,197,200,204,209,210,214,215,216,217,219,220,222,232,233,234,235,236,237,238,239,240,241,242,244,249,251,252,253,255,258,259,260,261,264,265,267,268,270,272,275,281,282,283,284,285,286,],[35,-26,-26,65,-25,67,-16,-29,-15,-41,-41,-41,-41,-41,-41,-41,-42,-17,-27,-68,-40,-40,-40,-40,-40,-40,-40,-40,156,-91,-82,159,-99,-79,-61,-60,-134,-129,-17,-128,-80,-132,-133,171,-130,-105,-79,-61,-60,-132,-133,-134,-65,-67,-32,-33,-34,-35,-36,-37,-38,-39,-116,-89,-40,-93,-95,-86,-87,-98,-73,-75,-76,-84,-85,-102,-131,-54,-55,-56,-57,-58,-59,205,-28,-64,-71,212,-88,-83,-83,-61,-17,-60,-92,-68,-104,231,-19,-90,236,237,-86,-87,-94,-65,-69,-18,-115,-51,-77,-78,-68,-72,-61,-64,-74,-101,-62,-65,-86,260,-103,-70,-64,-63,-127,270,-100,-108,-126,-63,-124,-109,-122,-114,-107,-126,-124,-110,]),'ConstanteInt':([32,70,90,91,92,99,100,110,114,136,143,155,158,181,198,199,200,201,203,221,223,225,226,238,245,247,250,257,],[38,-82,125,133,-123,-82,133,133,-82,133,133,133,125,133,125,-81,-82,-81,-106,125,125,133,-106,-82,133,-123,-82,133,]),'CorcheteDer':([38,43,63,69,121,122,123,124,125,126,130,131,132,133,134,135,144,165,167,168,169,170,174,175,176,177,178,179,187,196,211,219,233,236,237,239,240,242,252,260,],[-132,64,-16,-15,-129,-17,-128,-80,-132,-133,-79,-61,-60,-132,-133,-134,-19,-73,-75,-76,-84,-85,-54,-55,-56,-57,-58,-59,-20,-60,233,-87,-18,-77,-78,-72,-61,-74,-86,-63,]),'BraquetDer':([41,49,50,51,52,53,54,55,56,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,102,103,104,105,106,107,108,109,138,140,146,147,148,149,150,151,152,153,182,184,190,197,208,234,235,243,249,254,256,261,262,265,267,268,272,275,277,278,279,280,281,282,283,284,285,286,],[-50,71,-40,-40,-40,-40,-40,-40,-40,-41,-43,-41,-41,-41,-41,-41,-41,-42,-44,-45,-46,-47,-48,-49,-40,-40,-40,-40,-40,-40,-40,-40,-50,-40,-32,-33,-34,-35,-36,-37,-38,-39,207,-23,-88,-92,230,-115,-51,-40,-62,261,-40,-127,268,-100,-108,-126,-124,-109,-40,-40,281,282,-122,-114,-107,-126,-124,-110,]),'Lee':([41,50,51,52,53,54,55,56,72,74,75,76,77,78,79,80,102,103,104,105,106,107,108,109,114,138,140,158,190,197,234,235,243,249,256,261,265,267,268,272,275,277,278,281,282,283,284,285,286,],[58,58,58,58,58,58,58,58,-41,-41,-41,-41,-41,-41,-41,-42,58,58,58,58,58,58,58,58,-82,58,58,58,-88,-92,-115,-51,58,-62,58,-127,-100,-108,-126,-124,-109,58,58,-122,-114,-107,-126,-124,-110,]),'Escribe':([41,50,51,52,53,54,55,56,72,74,75,76,77,78,79,80,102,103,104,105,106,107,108,109,114,138,140,158,190,197,234,235,243,249,256,261,265,267,268,272,275,277,278,281,282,283,284,285,286,],[59,59,59,59,59,59,59,59,-41,-41,-41,-41,-41,-41,-41,-42,59,59,59,59,59,59,59,59,-82,59,59,59,-88,-92,-115,-51,59,-62,59,-127,-100,-108,-126,-124,-109,59,59,-122,-114,-107,-126,-124,-110,]),'Si':([41,50,51,52,53,54,55,56,72,74,75,76,77,78,79,80,102,103,104,105,106,107,108,109,114,138,140,158,190,197,234,235,243,249,256,261,265,267,268,272,275,277,278,281,282,283,284,285,286,],[60,60,60,60,60,60,60,60,-41,-41,-41,-41,-41,-41,-41,-42,60,60,60,60,60,60,60,60,-82,60,60,60,-88,-92,-115,-51,60,-62,60,-127,-100,-108,-126,-124,-109,60,60,-122,-114,-107,-126,-124,-110,]),'Mientras':([41,50,51,52,53,54,55,56,72,74,75,76,77,78,79,80,102,103,104,105,106,107,108,109,114,138,140,158,190,197,234,235,243,249,256,261,265,267,268,272,275,277,278,281,282,283,284,285,286,],[61,61,61,61,61,61,61,61,-41,-41,-41,-41,-41,-41,-41,-42,61,61,61,61,61,61,61,61,-82,61,61,61,-88,-92,-115,-51,61,-62,61,-127,-100,-108,-126,-124,-109,61,61,-122,-114,-107,-126,-124,-110,]),'Desde':([41,50,51,52,53,54,55,56,72,74,75,76,77,78,79,80,102,103,104,105,106,107,108,109,114,138,140,158,190,197,234,235,243,249,256,261,265,267,268,272,275,277,278,281,282,283,284,285,286,],[62,62,62,62,62,62,62,62,-41,-41,-41,-41,-41,-41,-41,-42,62,62,62,62,62,62,62,62,-82,62,62,62,-88,-92,-115,-51,62,-62,62,-127,-100,-108,-126,-124,-109,62,62,-122,-114,-107,-126,-124,-110,]),'Igual':([48,57,63,69,88,93,94,111,137,194,195,217,233,],[-17,-61,-16,-15,-53,-111,-17,155,181,-61,-17,-53,-18,]),'Regresa':([50,51,52,53,54,55,56,72,74,75,76,77,78,79,80,102,103,104,105,106,107,108,109,114,140,158,190,197,234,235,243,249,256,261,265,267,268,272,275,277,278,281,282,283,284,285,286,],[81,81,81,81,81,81,81,-41,-41,-41,-41,-41,-41,-41,-42,81,81,81,81,81,81,81,81,-82,81,81,-88,-92,-115,-51,81,-62,81,-127,-100,-108,-126,-124,-109,81,81,-122,-114,-107,-126,-124,-110,]),'SignoMultDiv':([63,69,118,119,122,123,124,125,126,131,132,133,134,162,163,167,168,169,170,175,176,177,178,194,195,196,217,219,233,236,237,240,252,260,270,],[-16,-15,-61,-60,-17,-128,-80,-132,-133,-61,-60,-132,-133,-86,-87,201,-76,-84,-85,-86,-87,-84,-85,-61,-17,-60,-86,-87,-18,-77,-78,-61,-86,-63,-63,]),'SignoSumRest':([63,69,118,119,121,122,123,124,125,126,131,132,133,134,162,163,165,167,168,169,170,175,176,177,178,194,195,196,217,219,233,236,237,240,242,252,260,270,],[-16,-15,-61,-60,-129,-17,-128,-80,-132,-133,-61,-60,-132,-133,-86,-87,199,-75,-76,-84,-85,-86,-87,-84,-85,-61,-17,-60,-86,-87,-18,-77,-78,-61,-74,-86,-63,-63,]),'OperadorLogico':([63,69,121,122,123,124,125,126,129,130,131,132,133,134,135,165,167,168,169,170,173,174,175,176,177,178,179,196,204,219,233,236,237,239,240,242,252,260,],[-16,-15,-129,-17,-128,-80,-132,-133,-105,-79,-61,-60,-132,-133,-134,-73,-75,-76,-84,-85,-131,-54,-55,-56,-57,-58,-59,-60,226,-87,-18,-77,-78,-72,-61,-74,-86,-63,]),'SignoLogico':([63,69,121,122,123,124,125,126,128,129,130,131,132,133,134,135,165,167,168,169,170,172,173,174,175,176,177,178,179,196,204,219,233,236,237,239,240,242,252,255,260,],[-16,-15,-129,-17,-128,-80,-132,-133,-130,-105,-79,-61,-60,-132,-133,-134,-73,-75,-76,-84,-85,203,-131,-54,-55,-56,-57,-58,-59,-60,-104,-87,-18,-77,-78,-72,-61,-74,-86,-103,-63,]),'Hasta':([63,69,121,122,123,124,125,126,130,131,132,133,134,135,165,167,168,169,170,174,175,176,177,178,179,196,206,219,228,233,236,237,239,240,242,252,260,],[-16,-15,-129,-17,-128,-80,-132,-133,-79,-61,-60,-132,-133,-134,-73,-75,-76,-84,-85,-54,-55,-56,-57,-58,-59,-60,-112,-87,247,-18,-77,-78,-72,-61,-74,-86,-63,]),'Hacer':([63,69,121,122,123,124,125,126,130,131,132,133,134,135,165,167,168,169,170,174,175,176,177,178,179,196,219,233,236,237,239,240,242,252,260,263,269,273,],[-16,-15,-129,-17,-128,-80,-132,-133,-79,-61,-60,-132,-133,-134,-73,-75,-76,-84,-85,-54,-55,-56,-57,-58,-59,-60,-87,-18,-77,-78,-72,-61,-74,-86,-63,-113,-125,276,]),'ConstanteFloat':([70,90,91,92,99,100,110,114,136,143,155,158,181,198,199,200,201,203,221,223,225,226,238,245,247,250,257,],[-82,126,134,-123,-82,134,134,-82,134,134,134,126,134,126,-81,-82,-81,-106,126,126,134,-106,-82,134,-123,-82,134,]),'ConstanteChar':([70,90,91,92,99,100,110,136,143,155,181,198,200,203,225,226,238,245,247,250,257,],[-82,120,135,-123,-82,135,135,135,135,135,135,120,-82,-106,135,-106,-82,135,-123,-82,135,]),'Entonces':([171,202,],[-125,224,]),'Haz':([205,227,],[-125,246,]),'Sino':([261,266,],[-126,271,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'goto':([3,271,],[4,274,]),'programaGlobal':([5,13,19,],[6,20,28,]),'variables':([5,13,19,65,67,],[7,7,7,96,96,]),'definirFuncion':([5,7,13,19,],[8,12,8,8,]),'addEndFunc':([8,12,],[13,19,]),'definirTipoVariable':([9,29,],[14,36,]),'popGoto':([11,281,],[18,283,]),'definirVariable':([15,37,],[21,42,]),'tipoIdentificadorDeclaracion':([15,37,],[22,22,]),'arrayDeclaracion':([15,37,],[24,24,]),'defineTipo':([22,31,],[30,37,]),'modificarFuncionActual':([25,26,],[33,34,]),'validarInt':([38,125,133,],[43,169,177,]),'parametrosDeclaracion':([39,40,],[44,47,]),'parametros':([39,40,139,],[45,45,183,]),'estatutoVoid':([41,138,],[49,182,]),'asignacion':([41,50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,138,140,158,243,256,277,278,],[50,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,50,72,72,72,72,72,72,]),'lectura':([41,50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,138,140,158,243,256,277,278,],[51,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,51,74,74,74,74,74,74,]),'escritura':([41,50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,138,140,158,243,256,277,278,],[52,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,52,75,75,75,75,75,75,]),'si':([41,50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,138,140,158,243,256,277,278,],[53,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,53,76,76,76,76,76,76,]),'mientras':([41,50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,138,140,158,243,256,277,278,],[54,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,54,77,77,77,77,77,77,]),'desde':([41,50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,138,140,158,243,256,277,278,],[55,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,55,78,78,78,78,78,78,]),'llamarFuncion':([41,50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,138,140,158,243,256,277,278,],[56,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,56,79,79,79,79,79,79,]),'tipoIdentificador':([41,50,51,52,53,54,55,56,62,89,90,91,100,102,103,104,105,106,107,108,109,110,136,138,140,143,155,158,181,191,198,221,223,225,243,245,256,257,277,278,],[57,57,57,57,57,57,57,57,93,113,118,131,131,57,57,57,57,57,57,57,57,131,131,57,57,131,131,194,131,113,118,240,240,131,57,131,57,131,57,57,]),'array':([41,50,51,52,53,54,55,56,62,89,90,91,100,102,103,104,105,106,107,108,109,110,136,138,140,143,155,158,181,191,198,221,223,225,243,245,256,257,277,278,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'validarFuncion':([48,122,195,],[68,166,218,]),'validarIdentificador':([48,94,122,195,],[69,69,69,69,]),'estatuto':([50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,140,158,243,256,277,278,],[73,82,83,84,85,86,87,146,147,148,149,150,151,152,153,184,192,254,262,279,280,]),'regresa':([50,51,52,53,54,55,56,102,103,104,105,106,107,108,109,140,158,243,256,277,278,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'validarVariable':([57,118,131,194,240,],[88,162,175,217,252,]),'variablesLocales':([65,67,],[95,98,]),'addVarParametro':([66,],[97,]),'addLista':([70,99,114,200,238,250,],[100,143,158,143,143,143,]),'addEndProgram':([71,],[101,]),'noReturn':([72,74,75,76,77,78,79,],[102,103,104,105,106,107,108,]),'siReturn':([80,],[109,]),'iniciarListaDir':([88,217,],[111,111,]),'valoresLectura':([89,191,],[112,214,]),'definirEscritura':([90,198,],[115,220,]),'asignarValorEscritura':([90,198,],[116,116,]),'exprecionArismetica':([90,91,100,110,136,143,155,158,181,198,221,225,245,257,],[117,130,130,130,130,130,130,193,130,117,239,130,130,130,]),'llamarFuncionAsignacion':([90,91,100,110,136,143,155,158,181,198,221,223,225,245,257,],[119,132,132,132,132,132,132,196,132,119,196,196,132,132,132,]),'asignarMultDiv':([90,91,100,110,136,143,155,158,181,198,221,223,225,245,257,],[121,121,121,121,121,121,121,121,121,121,121,242,121,121,121,]),'asignarValorArismetico':([90,91,100,110,136,143,155,158,181,198,221,223,225,245,257,],[123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,]),'valor':([90,91,100,110,136,143,155,158,181,198,221,223,225,245,257,],[124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,]),'exprecionLogica':([91,136,225,],[127,180,244,]),'asignarOperadorLogico':([91,136,225,245,],[128,128,128,255,]),'asignarValor':([91,100,110,136,143,155,181,225,245,257,],[129,144,154,129,186,189,206,129,129,263,]),'gotoM':([92,247,],[136,257,]),'validarIdDesde':([93,],[137,]),'parametrosLlamada':([99,200,238,],[141,222,251,]),'valoresLlamada':([99,200,238,250,],[142,142,142,258,]),'llamarMaquinaVirtual':([101,],[145,]),'cuadruploLectura':([113,],[157,]),'cuadruploEscritura':([116,],[160,]),'valorFinal':([117,130,],[161,174,]),'validarLlamada':([119,132,196,],[163,176,219,]),'validarChar':([120,135,],[164,179,]),'cuadruploSR':([121,],[165,]),'cuadruploMD':([123,],[167,]),'addListaVariables':([124,],[168,]),'validarFloat':([126,134,],[170,178,]),'cuadruploSignoLogico':([128,],[172,]),'addVariableLogica':([129,],[173,]),'goSub':([141,222,251,],[185,241,259,]),'cerrarListaArray':([144,210,],[187,232,]),'regresaCuadruplo':([154,],[188,]),'gotoF':([171,205,269,],[202,227,273,]),'cuadruploOperadorLogico':([173,],[204,]),'validarRegresa':([184,],[208,]),'asignarValorFuncion':([185,241,259,],[209,253,264,]),'paramFuncion':([186,],[210,]),'verArray':([187,],[211,]),'validarDirArray':([189,],[213,]),'cerrarLista':([192,193,],[215,216,]),'addOperador':([199,201,],[221,223,]),'addOperadorLogico':([203,226,],[225,245,]),'asignarDesde':([206,],[228,]),'popVars':([207,230,],[229,248,]),'sino':([261,],[265,]),'popGotoFs':([261,268,284,],[266,272,285,]),'popGotoF':([261,],[267,]),'comparaDesde':([263,],[269,]),'popGotoM':([272,285,],[275,286,]),'addUnoVariable':([282,],[284,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> Programa Identificador goto PuntoComa programaGlobal Principal popGoto ParentecisIzq ParentecisDer BraquetIzq estatutoVoid BraquetDer addEndProgram llamarMaquinaVirtual','programa',14,'p_programa','main.py',165),
  ('llamarMaquinaVirtual -> <empty>','llamarMaquinaVirtual',0,'p_llamarMaquinaVirtual','main.py',201),
  ('programaGlobal -> variables definirFuncion addEndFunc programaGlobal','programaGlobal',4,'p_programaGlobal','main.py',207),
  ('programaGlobal -> variables','programaGlobal',1,'p_programaGlobal','main.py',208),
  ('programaGlobal -> definirFuncion addEndFunc programaGlobal','programaGlobal',3,'p_programaGlobal','main.py',209),
  ('programaGlobal -> <empty>','programaGlobal',0,'p_programaGlobal','main.py',210),
  ('variables -> Var definirTipoVariable','variables',2,'p_variables','main.py',215),
  ('definirTipoVariable -> Tipo definirVariable PuntoComa','definirTipoVariable',3,'p_definirTipoVariable','main.py',222),
  ('definirTipoVariable -> Tipo definirVariable PuntoComa definirTipoVariable','definirTipoVariable',4,'p_definirTipoVariable','main.py',223),
  ('definirVariable -> tipoIdentificadorDeclaracion defineTipo','definirVariable',2,'p_definirVariable','main.py',228),
  ('definirVariable -> tipoIdentificadorDeclaracion Coma defineTipo definirVariable','definirVariable',4,'p_definirVariable','main.py',229),
  ('tipoIdentificadorDeclaracion -> Identificador','tipoIdentificadorDeclaracion',1,'p_tipoIdentificadorDeclaracion','main.py',237),
  ('tipoIdentificadorDeclaracion -> arrayDeclaracion','tipoIdentificadorDeclaracion',1,'p_tipoIdentificadorDeclaracion','main.py',238),
  ('arrayDeclaracion -> Identificador CorcheteIzq ConstanteInt validarInt CorcheteDer','arrayDeclaracion',5,'p_arrayDeclaracion','main.py',244),
  ('tipoIdentificador -> Identificador validarIdentificador','tipoIdentificador',2,'p_tipoIdentificador','main.py',253),
  ('tipoIdentificador -> array','tipoIdentificador',1,'p_tipoIdentificador','main.py',254),
  ('validarIdentificador -> <empty>','validarIdentificador',0,'p_validarIdentificador','main.py',260),
  ('array -> Identificador CorcheteIzq addLista asignarValor cerrarListaArray verArray CorcheteDer','array',7,'p_array','main.py',269),
  ('cerrarListaArray -> <empty>','cerrarListaArray',0,'p_cerrarListaArray','main.py',274),
  ('verArray -> <empty>','verArray',0,'p_verArray','main.py',287),
  ('definirFuncion -> Funcion TipoRetorno Identificador modificarFuncionActual ParentecisIzq parametrosDeclaracion ParentecisDer variablesLocales BraquetIzq estatutoVoid BraquetDer popVars','definirFuncion',12,'p_definirFuncion','main.py',400),
  ('definirFuncion -> Funcion Tipo Identificador modificarFuncionActual ParentecisIzq parametrosDeclaracion ParentecisDer variablesLocales BraquetIzq estatuto validarRegresa BraquetDer popVars','definirFuncion',13,'p_definirFuncion','main.py',401),
  ('validarRegresa -> <empty>','validarRegresa',0,'p_validarRegresa','main.py',410),
  ('modificarFuncionActual -> <empty>','modificarFuncionActual',0,'p_modificarFuncionActual','main.py',419),
  ('parametrosDeclaracion -> parametros','parametrosDeclaracion',1,'p_parametrosDeclaracion','main.py',439),
  ('parametrosDeclaracion -> <empty>','parametrosDeclaracion',0,'p_parametrosDeclaracion','main.py',440),
  ('parametros -> Tipo Identificador addVarParametro','parametros',3,'p_parametros','main.py',445),
  ('parametros -> Tipo Identificador addVarParametro Coma parametros','parametros',5,'p_parametros','main.py',446),
  ('addVarParametro -> <empty>','addVarParametro',0,'p_addVarParametro','main.py',450),
  ('variablesLocales -> variables','variablesLocales',1,'p_variablesLocales','main.py',477),
  ('variablesLocales -> <empty>','variablesLocales',0,'p_variablesLocales','main.py',478),
  ('estatuto -> asignacion noReturn estatuto','estatuto',3,'p_estatuto','main.py',482),
  ('estatuto -> lectura noReturn estatuto','estatuto',3,'p_estatuto','main.py',483),
  ('estatuto -> escritura noReturn estatuto','estatuto',3,'p_estatuto','main.py',484),
  ('estatuto -> si noReturn estatuto','estatuto',3,'p_estatuto','main.py',485),
  ('estatuto -> mientras noReturn estatuto','estatuto',3,'p_estatuto','main.py',486),
  ('estatuto -> desde noReturn estatuto','estatuto',3,'p_estatuto','main.py',487),
  ('estatuto -> llamarFuncion noReturn estatuto','estatuto',3,'p_estatuto','main.py',488),
  ('estatuto -> regresa siReturn estatuto','estatuto',3,'p_estatuto','main.py',489),
  ('estatuto -> <empty>','estatuto',0,'p_estatuto','main.py',490),
  ('noReturn -> <empty>','noReturn',0,'p_noReturn','main.py',494),
  ('siReturn -> <empty>','siReturn',0,'p_siReturn','main.py',499),
  ('estatutoVoid -> asignacion estatuto','estatutoVoid',2,'p_estatutoVoid','main.py',505),
  ('estatutoVoid -> lectura estatuto','estatutoVoid',2,'p_estatutoVoid','main.py',506),
  ('estatutoVoid -> escritura estatuto','estatutoVoid',2,'p_estatutoVoid','main.py',507),
  ('estatutoVoid -> si estatuto','estatutoVoid',2,'p_estatutoVoid','main.py',508),
  ('estatutoVoid -> mientras estatuto','estatutoVoid',2,'p_estatutoVoid','main.py',509),
  ('estatutoVoid -> desde estatuto','estatutoVoid',2,'p_estatutoVoid','main.py',510),
  ('estatutoVoid -> llamarFuncion estatuto','estatutoVoid',2,'p_estatutoVoid','main.py',511),
  ('estatutoVoid -> <empty>','estatutoVoid',0,'p_estatutoVoid','main.py',512),
  ('asignacion -> tipoIdentificador validarVariable iniciarListaDir Igual asignarValor validarDirArray PuntoComa','asignacion',7,'p_asignacion','main.py',517),
  ('validarDirArray -> <empty>','validarDirArray',0,'p_validarDirArray','main.py',545),
  ('iniciarListaDir -> <empty>','iniciarListaDir',0,'p_iniciarListaDir','main.py',553),
  ('asignarValor -> exprecionArismetica valorFinal','asignarValor',2,'p_asignarValor','main.py',564),
  ('asignarValor -> tipoIdentificador validarVariable','asignarValor',2,'p_asignarValor','main.py',565),
  ('asignarValor -> llamarFuncionAsignacion validarLlamada','asignarValor',2,'p_asignarValor','main.py',566),
  ('asignarValor -> ConstanteInt validarInt','asignarValor',2,'p_asignarValor','main.py',567),
  ('asignarValor -> ConstanteFloat validarFloat','asignarValor',2,'p_asignarValor','main.py',568),
  ('asignarValor -> ConstanteChar validarChar','asignarValor',2,'p_asignarValor','main.py',569),
  ('validarLlamada -> <empty>','validarLlamada',0,'p_validarLlamada','main.py',577),
  ('validarVariable -> <empty>','validarVariable',0,'p_validarVariable','main.py',581),
  ('llamarFuncion -> Identificador validarFuncion ParentecisIzq parametrosLlamada goSub asignarValorFuncion ParentecisDer PuntoComa','llamarFuncion',8,'p_llamarFuncion','main.py',603),
  ('llamarFuncionAsignacion -> Identificador validarFuncion ParentecisIzq parametrosLlamada goSub asignarValorFuncion ParentecisDer','llamarFuncionAsignacion',7,'p_llamarFuncionAsignacion','main.py',611),
  ('asignarValorFuncion -> <empty>','asignarValorFuncion',0,'p_asignarValorFuncion','main.py',618),
  ('goSub -> <empty>','goSub',0,'p_goSub','main.py',636),
  ('validarFuncion -> <empty>','validarFuncion',0,'p_validarFuncion','main.py',653),
  ('parametrosLlamada -> valoresLlamada','parametrosLlamada',1,'p_parametrosLlamada','main.py',669),
  ('parametrosLlamada -> <empty>','parametrosLlamada',0,'p_parametrosLlamada','main.py',670),
  ('valoresLlamada -> addLista asignarValor paramFuncion cerrarListaArray','valoresLlamada',4,'p_valoresLlamada','main.py',675),
  ('valoresLlamada -> addLista asignarValor paramFuncion cerrarListaArray Coma valoresLlamada','valoresLlamada',6,'p_valoresLlamada','main.py',676),
  ('paramFuncion -> <empty>','paramFuncion',0,'p_paramFuncion','main.py',680),
  ('exprecionArismetica -> asignarMultDiv cuadruploSR SignoSumRest addOperador exprecionArismetica','exprecionArismetica',5,'p_exprecionArismetica','main.py',718),
  ('exprecionArismetica -> asignarMultDiv cuadruploSR','exprecionArismetica',2,'p_exprecionArismetica','main.py',719),
  ('asignarMultDiv -> asignarValorArismetico cuadruploMD SignoMultDiv addOperador asignarMultDiv','asignarMultDiv',5,'p_asignarMultDiv','main.py',723),
  ('asignarMultDiv -> asignarValorArismetico cuadruploMD','asignarMultDiv',2,'p_asignarMultDiv','main.py',724),
  ('asignarValorArismetico -> valor addListaVariables','asignarValorArismetico',2,'p_asignarValorArismetico','main.py',728),
  ('asignarValorArismetico -> ParentecisIzq addLista estatuto cerrarLista ParentecisDer','asignarValorArismetico',5,'p_asignarValorArismetico','main.py',729),
  ('asignarValorArismetico -> ParentecisIzq addLista exprecionArismetica cerrarLista ParentecisDer','asignarValorArismetico',5,'p_asignarValorArismetico','main.py',730),
  ('valorFinal -> <empty>','valorFinal',0,'p_valorFinal','main.py',736),
  ('addListaVariables -> <empty>','addListaVariables',0,'p_addListaVariables','main.py',741),
  ('addOperador -> <empty>','addOperador',0,'p_addOperador','main.py',756),
  ('addLista -> <empty>','addLista',0,'p_addLista','main.py',762),
  ('cerrarLista -> <empty>','cerrarLista',0,'p_cerrarLista','main.py',769),
  ('valor -> ConstanteInt validarInt','valor',2,'p_valor','main.py',780),
  ('valor -> ConstanteFloat validarFloat','valor',2,'p_valor','main.py',781),
  ('valor -> tipoIdentificador validarVariable','valor',2,'p_valor','main.py',782),
  ('valor -> llamarFuncionAsignacion validarLlamada','valor',2,'p_valor','main.py',783),
  ('lectura -> Lee ParentecisIzq valoresLectura ParentecisDer PuntoComa','lectura',5,'p_lectura','main.py',791),
  ('valoresLectura -> tipoIdentificador cuadruploLectura','valoresLectura',2,'p_valoresLectura','main.py',795),
  ('valoresLectura -> tipoIdentificador cuadruploLectura Coma valoresLectura','valoresLectura',4,'p_valoresLectura','main.py',796),
  ('cuadruploLectura -> <empty>','cuadruploLectura',0,'p_cuadruploLectura','main.py',802),
  ('escritura -> Escribe ParentecisIzq definirEscritura ParentecisDer PuntoComa','escritura',5,'p_escritura','main.py',814),
  ('definirEscritura -> asignarValorEscritura cuadruploEscritura','definirEscritura',2,'p_definirEscritura','main.py',818),
  ('definirEscritura -> asignarValorEscritura cuadruploEscritura Coma definirEscritura','definirEscritura',4,'p_definirEscritura','main.py',819),
  ('asignarValorEscritura -> exprecionArismetica valorFinal','asignarValorEscritura',2,'p_asignarValorEscritura','main.py',824),
  ('asignarValorEscritura -> tipoIdentificador validarVariable','asignarValorEscritura',2,'p_asignarValorEscritura','main.py',825),
  ('asignarValorEscritura -> llamarFuncionAsignacion validarLlamada','asignarValorEscritura',2,'p_asignarValorEscritura','main.py',826),
  ('asignarValorEscritura -> ConstanteChar validarChar','asignarValorEscritura',2,'p_asignarValorEscritura','main.py',827),
  ('cuadruploEscritura -> <empty>','cuadruploEscritura',0,'p_cuadruploEscritura','main.py',835),
  ('si -> Si ParentecisIzq exprecionLogica ParentecisDer gotoF Entonces BraquetIzq estatuto BraquetDer sino','si',10,'p_si','main.py',846),
  ('exprecionLogica -> asignarOperadorLogico cuadruploSignoLogico SignoLogico addOperadorLogico exprecionLogica','exprecionLogica',5,'p_exprecionLogica','main.py',851),
  ('exprecionLogica -> asignarOperadorLogico cuadruploSignoLogico','exprecionLogica',2,'p_exprecionLogica','main.py',852),
  ('asignarOperadorLogico -> asignarValor addVariableLogica cuadruploOperadorLogico OperadorLogico addOperadorLogico asignarOperadorLogico','asignarOperadorLogico',6,'p_asignarOperadorLogico','main.py',857),
  ('asignarOperadorLogico -> asignarValor addVariableLogica cuadruploOperadorLogico','asignarOperadorLogico',3,'p_asignarOperadorLogico','main.py',858),
  ('addVariableLogica -> <empty>','addVariableLogica',0,'p_addSignoLogico','main.py',861),
  ('addOperadorLogico -> <empty>','addOperadorLogico',0,'p_addOperadorLogico','main.py',866),
  ('sino -> popGotoFs Sino goto BraquetIzq estatuto BraquetDer popGoto','sino',7,'p_sino','main.py',871),
  ('sino -> popGotoF','sino',1,'p_sino','main.py',872),
  ('mientras -> Mientras ParentecisIzq gotoM exprecionLogica ParentecisDer gotoF Haz BraquetIzq estatuto BraquetDer popGotoFs popGotoM','mientras',12,'p_mientras','main.py',877),
  ('desde -> Desde tipoIdentificador validarIdDesde Igual asignarValor asignarDesde Hasta gotoM asignarValor comparaDesde gotoF Hacer BraquetIzq estatuto BraquetDer addUnoVariable popGotoFs popGotoM','desde',18,'p_desde','main.py',881),
  ('validarIdDesde -> <empty>','validarIdDesde',0,'p_validarIdDesde','main.py',885),
  ('asignarDesde -> <empty>','asignarDesde',0,'p_asignarDesde','main.py',893),
  ('comparaDesde -> <empty>','comparaDesde',0,'p_comparaDesde','main.py',914),
  ('addUnoVariable -> <empty>','addUnoVariable',0,'p_addUnoVariable','main.py',935),
  ('regresa -> Regresa ParentecisIzq asignarValor regresaCuadruplo ParentecisDer PuntoComa','regresa',6,'p_regresa','main.py',978),
  ('regresaCuadruplo -> <empty>','regresaCuadruplo',0,'p_regresaCuadruplo','main.py',984),
  ('defineTipo -> <empty>','defineTipo',0,'p_defineTipo','main.py',1011),
  ('popVars -> <empty>','popVars',0,'p_popVars','main.py',1062),
  ('addEndFunc -> <empty>','addEndFunc',0,'p_addEndFunc','main.py',1086),
  ('addEndProgram -> <empty>','addEndProgram',0,'p_addEndProgram','main.py',1093),
  ('goto -> <empty>','goto',0,'p_goto','main.py',1106),
  ('popGoto -> <empty>','popGoto',0,'p_popGoto','main.py',1114),
  ('gotoM -> <empty>','gotoM',0,'p_gotoM','main.py',1120),
  ('popGotoM -> <empty>','popGotoM',0,'p_popGotoM','main.py',1126),
  ('gotoF -> <empty>','gotoF',0,'p_gotoF','main.py',1135),
  ('popGotoFs -> <empty>','popGotoFs',0,'p_popGotoFs','main.py',1147),
  ('popGotoF -> <empty>','popGotoF',0,'p_popGotoF','main.py',1153),
  ('cuadruploMD -> <empty>','cuadruploMD',0,'p_cuadruploMD','main.py',1165),
  ('cuadruploSR -> <empty>','cuadruploSR',0,'p_cuadruploSR','main.py',1202),
  ('cuadruploSignoLogico -> <empty>','cuadruploSignoLogico',0,'p_cuadruploSignoLogico','main.py',1237),
  ('cuadruploOperadorLogico -> <empty>','cuadruploOperadorLogico',0,'p_cuadruploOperadorLogico','main.py',1270),
  ('validarInt -> <empty>','validarInt',0,'p_validarInt','main.py',1555),
  ('validarFloat -> <empty>','validarFloat',0,'p_validarFloat','main.py',1580),
  ('validarChar -> <empty>','validarChar',0,'p_validarChar','main.py',1605),
  ('debugErrors -> <empty>','debugErrors',0,'p_debugErrors','main.py',1688),
]

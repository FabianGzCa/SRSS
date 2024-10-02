## Objetivo
How about trying to match a regular expression.

## Solución
Inspeccionamos el código:
```js
function send_request() {
		let val = document.getElementById("name").value;
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}
```

Vemos esa pista p.....F y conocemos algo que inicia similar picoCTF, tratemos de ingresarlo y obtenemos la flag
picoCTF{succ3ssfully_matchtheregex_08c310c6}

## Notas Adicionales


## Referencias

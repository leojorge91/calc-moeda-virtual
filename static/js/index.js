$('#btn_enviar').click(function(){

	var moeda = $('#moeda').val()
	var investimento = $('#investimento').val()

	$.ajax({
		url: 'consulta',
		type: 'GET',
		data: {moeda: moeda, investimento:investimento},
		dataType: 'json',
		success: function(data){
			console.log(data);
			$('#resultado').text("E possivel comprar " + data);
		},
		failure: function(data){
			console.log("Ocorreu um erro na execucao do ajax.");
		},
	});
});
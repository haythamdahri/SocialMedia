var toggle = document.getElementById('container');
var toggleContainer = document.getElementById('toggle-container');
var toggleNumber;





$(document).ready( function() {

$('#photoform .input-group, #photoprofilform .input-group').find(':text').val('');




	$("#btcoverchange, #btprofilchange").click(function() {
        $(".modal-footer").show();
        $("#photo, #photo1").hide();
        $(".uploadp, .uploadprogress").addClass('hidden');
        $("#photoform input[type=text], #photoprofilform input[type=text]").val('');
    });


    	$(document).on('change', '.btn-file :file', function() {
		var input = $(this),
			label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
		input.trigger('fileselect', [label]);
		});

    	$(document).on('change', '.btn-file1 :file', function() {
		var input = $(this),
			label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
		input.trigger('fileselect', [label]);
		});

		$('.btn-file :file').on('fileselect', function(event, label) {

		    var input = $(this).parents('.input-group').find(':text'),
		        log = label;

		    if( input.length ) {
		        input.val(log);
		    } else {
		        if( log ) console.log(log);
		    }

		});

		$('.btn-file1 :file').on('fileselect', function(event, label) {

		    var input = $(this).parents('.input-group').find(':text'),
		        log = label;

		    if( input.length ) {
		        input.val(log);
		    } else {
		        if( log ) console.log(log);
		    }

		});

		function readURL(input) {
		    if (input.files && input.files[0]) {
		        var reader = new FileReader();

		        reader.onload = function (e) {
		            $('#img-upload').attr('class', 'img-thumbnail');
		            $('#img-upload').attr('src', e.target.result);
		            $('#photo').fadeIn(1500);
		        }

		        reader.readAsDataURL(input.files[0]);
		    }
		}

		function readURL1(input) {
		    if (input.files && input.files[0]) {
		        var reader = new FileReader();

		        reader.onload = function (e) {
		            $('#img-upload1').attr('class', 'img-thumbnail');
		            $('#img-upload1').attr('src', e.target.result);
		            $('#photo1').fadeIn(1500);
		        }

		        reader.readAsDataURL(input.files[0]);
		    }
		}

		$("#imgInp").change(function(){
		    readURL(this);
		});

		$("#imgInp1").change(function(){
		    readURL1(this);
		});

		$(".blue").hover(function(){
			$(".blue").css('opacity','1');
		},function(){
			$(".blue").css('opacity','0.3');
		});

		$(".green").hover(function(){
			$(".green").css('padding','20');
		},function(){
			$(".green").css('padding','');
		});



	});

toggle.addEventListener('click', function() {
	toggleNumber = !toggleNumber;
	if (toggleNumber) {
		toggleContainer.style.clipPath = 'inset(0 0 0 50%)';
		toggleContainer.style.backgroundColor = '#D74046';
		$(".signup").slideToggle(1000);
    	$('.signin').slideToggle(1000);
    	$(document).prop("title", "S'inscrire");
	} else {
		toggleContainer.style.clipPath = 'inset(0 50% 0 0)';
		toggleContainer.style.backgroundColor = 'dodgerblue';
		$(".signup").slideToggle(1000);
    	$('.signin').slideToggle(1000);
    	$(document).prop('title', 'Se Connecter');
	}
	console.log(toggleNumber)
});

$("#resetpassword").click(function(){
	$("#resetpasswordmodal").fadeIn(750);
});





/*recherche sur la table experience*/
$(document).ready(function(){

  $(function() {
    $("#titre_experience").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "experience-searchJSON",
                dataType: "json",
                data: {
                    featureClass: "P",
                    style: "full",
                    maxRows: 12,
                    name_startsWith: request.term
                },
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            label: item,
                            value: item
                        }
                    }));
                }
            });
        },
        minLength: 2,
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
});
});


/*recherche sur la table institution*/
$(document).ready(function(){

  $(function() {
    $("#nom_institution").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "institution-searchJSON",
                dataType: "json",
                data: {
                    featureClass: "P",
                    style: "full",
                    maxRows: 12,
                    name_startsWith: request.term
                },
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            label: item,
                            value: item
                        }
                    }));
                }
            });
        },
        minLength: 2,
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
});
});

/*recherche sur la table ressource*/
$(document).ready(function(){

  $(function() {
    $("#ressource_titre").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "ressource-searchJSON",
                dataType: "json",
                data: {
                    featureClass: "P",
                    style: "full",
                    maxRows: 12,
                    name_startsWith: request.term
                },
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            label: item,
                            value: item
                        }
                    }));
                }
            });
        },
        minLength: 2,
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
});
});

/*recherche sur la table auteur*/
$(document).ready(function(){

  $(function() {
    $("#auteur_nom").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "auteur-searchJSON",
                dataType: "json",
                data: {
                    featureClass: "P",
                    style: "full",
                    maxRows: 12,
                    name_startsWith: request.term
                },
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            label: item,
                            value: item
                        }
                    }));
                }
            });
        },
        minLength: 2,
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
});
});


/*recherche sur le xml rezo*/
$(document).ready(function(){

  $(function() {
    $("#thesaurus").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "thesaurus-searchJSON",
                dataType: "json",
                data: {
                    featureClass: "P",
                    style: "full",
                    maxRows: 12,
                    name_startsWith: request.term
                },
                success: function(data) {
                    response($.map(data, function(item) {
                        return {
                            label: item,
                            value: item
                        }
                    }));
                }
            });
        },
        minLength: 2,
        open: function() {
            $(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function() {
            $(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
    });
});
});

/* LiveSearch filtre sur les addRemoveWidget */
$(document).ready(function(){

$('[name="add_remove_widget_input_livesearch"]').each(function() {
    var elem = $(this);

    // Save current value of element
    elem.data('oldVal', elem.val());

    // Look for changes in the value
    elem.bind("propertychange keyup input paste", function(event){
        // If value has changed...
        if (elem.data('oldVal') != elem.val()) {

            // Updated stored value
            elem.data('oldVal', elem.val());

            // Filter in the fromBox
            var originalListName = elem.attr('id') + '_original_list:list';
            var originalList = $('[name="' + originalListName + '"]');

            // Clear fromBox
            var fromBoxId = elem.attr('from_box');
            var fromBox = $('#'+fromBoxId);
            fromBox.empty();

            // Compare search filter string to each value of original list
            originalList.each(function() {
                var fromBoxId = elem.attr('from_box');
                var toBoxId = elem.attr('to_box');
                var filteredFromList = [];

                var item = $(this);
                // Check to compare the search filter to the original list
                if (item.val().toUpperCase().indexOf(elem.val().toUpperCase()) > -1
                        || elem.val() === '')
                {
                    // Check if option is not in toBox
                    if ($('#' + toBoxId + ' option[value="' + item.attr('key') +'"]').length <= 0)
                    {
                        // Add the option in fromBox
                        optionHtml = '<option value="' + item.attr('key') +'">' + item.val() + '</option>';
                        $('#'+fromBoxId).append($(optionHtml));
                    }
                }
            });

        }
    });
});
});
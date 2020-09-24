String.prototype.escape = function() {
    var tagsToReplace = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#130;',
        '-': '&#150;'
    };
    return this.replace(/[&<>\"\'-]/g, function(tag) {
        return tagsToReplace[tag] || tag;
    });
};

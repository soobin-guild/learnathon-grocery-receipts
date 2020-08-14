document.getElementById("imagefile").addEventListener(
  "change",
  function () {
    console.log("file uploaded");
    var reader = new FileReader();
    var fileByteArray = [];
    reader.readAsArrayBuffer(this.files[0]);
    reader.onloadend = function (evt) {
      if (evt.target.readyState == FileReader.DONE) {
        var arrayBuffer = evt.target.result,
          array = new Uint8Array(arrayBuffer);
        for (var i = 0; i < array.length; i++) {
          fileByteArray.push(array[i]);
        }
      }
    };

    if (fileByteArray.length != null) {
      var apigClient = apigClientFactory.newClient({
        apiKey: "LEIyDhJ8qg1dQf4vcUo583BinpnGff7D9Mr39W4H",
      });
      var params = {
        image: fileByteArray,
      };
      var body = {};
      apigClient
        .recommendRecipesOptions(params, body)
        .then(function (result) {
          console.log(JSON.parse(result));
        })
        .catch(function (result) {
          console.log(`error ${result.status} - ${result.statusText}`);
        });
    }
  },
  false
);

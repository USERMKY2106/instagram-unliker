import cronitor

cronitor.api_key = "c25b3667dcbf42498c6a86b01dd9cb3c"
cronitor.Monitor.put(
    key="Instagran Unliker",
    type="job",
    schedule="0 0 * * *"  

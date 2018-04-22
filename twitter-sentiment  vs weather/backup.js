var OHscores = [];
            var CAscores = [];
            var TXscores = [];
            var GAscores = [];
            var NYscores = [];
            var ILscores = [];
            var AKscores = [];
            var AZscores = [];
            var FLscores = [];
            var KYscores = [];
            var MIscores = [];
            var MNscores = [];
            var MSscores = [];
            var MOscores = [];
            var NEscores = [];
            var NVscores = [];
            var MNscores = [];
            var NMscores = [];
            var ORscores = [];

            var OHcounts = [];
            var CAcounts = [];
            var TXcounts = [];
            var GAcounts = [];
            var NYcounts = [];
            var ILcounts = [];
            var AKcounts = [];
            var AZcounts = [];
            var FLcounts = [];
            var KYcounts = [];
            var MIcounts = [];
            var MNcounts = [];
            var MScounts = [];
            var MOcounts = [];
            var NEcounts = [];
            var NVcounts = [];
            var NMcounts = [];
            var NMcounts = [];
            var ORcounts = [];

                    data.forEach(function(d) {
                        if (d.state == "OH"){
                            OHscores.push(d.score);
                            OHcounts.push(d.count);
                        }
                        if (d.state == "CA"){
                            CAscores.push(d.score);
                            CAcounts.push(d.count);
                        }
                        if (d.state == "TX"){
                            TXscores.push(d.score);
                            TXcounts.push(d.count);
                        }
                        if (d.state == "GA"){
                            GAscores.push(d.score);
                            GAcounts.push(d.count);
                        }
                        if (d.state == "NY"){
                            NYscores.push(d.score);
                            NYcounts.push(d.count);    
                        }
                        if (d.state == "IL"){
                            ILscores.push(d.score);
                            ILcounts.push(d.count);
                        }
                        if (d.state == "AK"){
                            AKscores.push(d.score);
                            AKcounts.push(d.count);
                        }
                        if (d.state == "AZ"){
                            AZscores.push(d.score);
                            AZcounts.push(d.count);
                        }
                        if (d.state == "FL"){
                            FLscores.push(d.score);
                            FLcounts.push(d.count);
                        }
                        if (d.state == "KY"){
                            KYscores.push(d.score);
                            KYcounts.push(d.count);
                        }
                        if (d.state == "MI"){
                            MIscores.push(d.score);
                            MIcounts.push(d.count);
                        }
                        if (d.state == "MN"){
                            MNscores.push(d.score);
                            MNcounts.push(d.count);
                        }
                        if (d.state == "MS"){
                            MSscores.push(d.score);
                            MScounts.push(d.count);
                        }
                        if (d.state == "MO"){
                            MOscores.push(d.score);
                            MOcounts.push(d.count);
                        }
                        if (d.state == "NE"){
                            NEscores.push(d.score);
                            NEcounts.push(d.count);
                        }
                        if (d.state == "NV"){
                            NVscores.push(d.score);
                            NVcounts.push(d.count);
                        }
                        if (d.state == "NM"){
                            NMscores.push(d.score);
                            NMcounts.push(d.count);
                        }
                        if (d.state == "OR"){
                            ORscores.push(d.score);
                            ORcounts.push(d.count);
                        }
                        

                    });
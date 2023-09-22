const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {

    entry: "./assets/scripts/index.js",

    output: {

        filename: "bundle.js",
        path: path.resolve(__dirname, "jobsearch", "static", "jobsearch", "scripts")
    },

    module: {

        rules: [

            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "sass-loader"
                ],
            },
        ],
    },

    plugins: [

        new MiniCssExtractPlugin({

            filename: "../styles/bundle.css",

        }),
    ],

}
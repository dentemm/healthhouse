const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const NewExtractTextPlugin = require('mini-css-extract-plugin');

module.exports = () => {

  const CSSExtract = new NewExtractTextPlugin({
    filename: 'styles.css'
  });

  return {
    entry: './healthhouse/static/js/index.js',
    output: {
      path: path.join(__dirname, './healthhouse/static/test'),
      filename: 'bundle.js'
    },
    module: {
      rules: [
        {
          loader: 'babel-loader',
          test: /\.js$/,
          exclude: /node_modules/
        },
        {
          test : /\.css$/,
          use: [
            NewExtractTextPlugin.loader,
            'css-loader',
            'sass-loader'
          ]
          // use: CSSExtract.extract({
          //   fallback: 'style-loader',
          //   use: [
          //     'css-loader',
          //     'sass-loader'
          //   ]
          // })
        }
        // {
        //   test: /\.s?css$/,
        //   use: ExtractTextPlugin.extract({
        //     fallback: 'style-loader',
        //     use: [
        //       'style-loader',
        //       'css-loader',
        //       'sass-loader'
        //     ]
        //   })
        // }
      ]
    },
    devtool: 'cheap-module-eval-source-map',
    plugins: [
      CSSExtract
    ]
  };
}
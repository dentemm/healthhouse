const path = require('path');
const ExtractTextPlugin = require('mini-css-extract-plugin');

module.exports = () => {

  const CSSExtract = new ExtractTextPlugin({
    filename: 'styles.css'
  });

  return {
    entry: './healthhouse/static/js/index.js',
    output: {
      path: path.join(__dirname, './healthhouse/static/bundle'),
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
          test : /\.s?css$/,
          use: [
            ExtractTextPlugin.loader,
            'css-loader',
            'sass-loader'
          ]
        }
      ]
    },
    devtool: 'cheap-module-eval-source-map',
    plugins: [
      CSSExtract
    ]
  };
}
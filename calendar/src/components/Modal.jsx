import * as React from 'react';

class Modal extends React.Component {

  render() {
    return (
      <div className="modal fade" id="calendarModal" tabIndex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div className="modal-dialog modal-dialog-centered" role="document">
          <div className="modal-content">
            <div className="modal-header justify-content-end">
              <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true" className="icon-x"></span>
              </button>
            </div>
            <div className="modal-body text-center">
              <h3>Modal title</h3>
              <p>{`${this.props.day ? this.props.day.format('D') : 'nog niks'}`}</p>  
            </div>
            <div className="modal-footer">
              <button type="button" className="btn btn-primary btn-block">Save changes</button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Modal;
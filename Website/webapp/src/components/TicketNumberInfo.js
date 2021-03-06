import React from 'react'
import CloseButton from './CloseButton';

const TicketNumberInfo = (props) =>
  <div className="ticket-number">
    #{props.number}
    <CloseButton onRemove={() => props.onRemove(props.number)} allowRemove={true} />
  </div>



export default TicketNumberInfo;
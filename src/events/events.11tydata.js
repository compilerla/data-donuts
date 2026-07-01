// /event/:slug/
const permalink = ({ page: { fileSlug } }) => `/event/${fileSlug}/`;

export default {
  layout: "event",
  permalink,
  tags: "events",

  location: "LACI",
  start_time: "8:00am",
  end_time: "10:00am",
};

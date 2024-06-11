import NavBar from "./NavBar/NavBar.js";
import Heros from "./Heros/Heros.js";
import SecondSection from "./SecondSection/SecondSection.js";
import QuoteSection from "./QuoteSection/QuoteSection.js";
import DivisionalSection from "./DivisionalSection/DivisionalSection.js";
import CourseCard from "./CourseCard/CourseCard.js";
import CommunitySection from "./CommunitySection/CommunitySection.js";
import TestimonialSection from "./TestimonialSection/TestimonialSection.js";
import NewsletterSection from "./NewsletterSection/NewsletterSection.js";
import Footer from "./Footer/Footer.js";

/**
 * Renders the landing page component.
 * @returns {JSX.Element} The landing page component.
 */
function LandingPage() {
  return (
    <div className="overflow-y-scroll no-scrollbar">
      <NavBar />
      <Heros />
      <SecondSection />
      <QuoteSection />
      <DivisionalSection />
      <CourseCard />
      <CommunitySection />
      <TestimonialSection />
      <NewsletterSection />
      <Footer />
    </div>
  );
}

export default LandingPage;
